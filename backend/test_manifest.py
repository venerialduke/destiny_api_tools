#!/usr/bin/env python3
"""
Test script for manifest download and database population.
"""

import os
import sys
import time

# Add the backend directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.services.manifest_service import ManifestService
from app.services.database_service import DatabaseService


def progress_callback(percentage, downloaded, total):
    """Callback for download progress."""
    mb_downloaded = downloaded / (1024 * 1024)
    mb_total = total / (1024 * 1024)
    print(f"\rDownloading: {percentage:.1f}% ({mb_downloaded:.1f}MB / {mb_total:.1f}MB)", end='', flush=True)


def main():
    """Test manifest operations."""
    print("=== Destiny Manifest Test ===\n")
    
    # Initialize manifest service
    manifest_service = ManifestService()
    
    try:
        # 1. Check current status
        print("1. Checking manifest status...")
        stats = manifest_service.get_database_stats()
        print(f"   Status: {stats.get('status', 'unknown')}")
        
        if stats.get('status') == 'ready':
            print(f"   Current version: {stats.get('version', 'unknown')}")
            print(f"   Last updated: {stats.get('last_updated', 'unknown')}")
            print(f"   Database size: {stats.get('file_size_mb', 0)}MB")
            print(f"   Total definitions: {stats.get('total_definitions', 0)}")
        
        # 2. Check for updates
        print("\n2. Checking for updates...")
        needs_update = manifest_service.needs_update()
        print(f"   Update needed: {needs_update}")
        
        if needs_update:
            print("\n3. Downloading manifest...")
            start_time = time.time()
            
            success = manifest_service.update_manifest(progress_callback)
            
            end_time = time.time()
            print(f"\n   Update completed in {end_time - start_time:.1f} seconds")
            print(f"   Success: {success}")
            
            if success:
                # Get updated stats
                stats = manifest_service.get_database_stats()
                print(f"\n   New database stats:")
                print(f"   Version: {stats.get('version', 'unknown')}")
                print(f"   Size: {stats.get('file_size_mb', 0)}MB")
                print(f"   Total definitions: {stats.get('total_definitions', 0)}")
                
                # Show table counts
                table_counts = stats.get('table_counts', {})
                for table, count in table_counts.items():
                    print(f"   {table}: {count:,} entries")
        else:
            print("   Manifest is up to date")
        
        # 4. Test database queries
        print("\n4. Testing database queries...")
        
        db_path = os.path.join('data', 'manifest.db')
        if os.path.exists(db_path):
            db_service = DatabaseService(db_path)
            
            # Test item lookup
            test_hash = 1384536110  # Example: Gjallarhorn hash (if available)
            item = db_service.get_item_by_hash(test_hash)
            if item:
                print(f"   Found item: {item['display_name']}")
            else:
                print(f"   Item with hash {test_hash} not found")
            
            # Test search
            search_results = db_service.search_items(query='gjallarhorn', limit=5)
            print(f"   Search results for 'gjallarhorn': {len(search_results['items'])} items")
            for item in search_results['items'][:3]:
                print(f"     - {item['display_name']} (hash: {item['hash']})")
            
            # Test weapon search
            weapon_results = db_service.search_items(is_weapon=True, tier_type=6, limit=5)  # Exotic weapons
            print(f"   Exotic weapons found: {weapon_results['total']}")
            for weapon in weapon_results['items'][:3]:
                print(f"     - {weapon['display_name']} (tier: {weapon['tier_type']})")
        
        print("\n=== Test Complete ===")
        
    except Exception as e:
        print(f"\nError during test: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()