#!/usr/bin/env python3
"""
Test script for the enhanced manifest system.
"""

import os
import sys
sys.path.append('backend')

from backend.app.services.enhanced_manifest_service import EnhancedManifestService

def test_enhanced_manifest():
    """Test the enhanced manifest download and processing system."""
    print("=== TESTING ENHANCED MANIFEST SYSTEM ===")
    
    service = EnhancedManifestService()
    
    # Test manifest update
    print("\n1. Testing manifest update...")
    success = service.update_manifest()
    
    if not success:
        print("ERROR: Manifest update failed!")
        return False
    
    print("SUCCESS: Manifest update completed!")
    
    # Test available tables
    print("\n2. Testing available tables...")
    tables = service.get_available_tables()
    print(f"Available tables ({len(tables)}):")
    for table in sorted(tables):
        print(f"  - {table}")
    
    # Test flattened database stats
    print("\n3. Testing flattened database stats...")
    stats = service.get_flattened_stats()
    
    print(f"Total flattened records: {stats.get('total_records', 0):,}")
    print(f"Data type distribution:")
    for data_type, count in stats.get('type_distribution', {}).items():
        print(f"  - {data_type}: {count:,}")
    
    print(f"Top 10 tables by record count:")
    table_dist = stats.get('table_distribution', {})
    for table, count in sorted(table_dist.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  - {table}: {count:,}")
    
    # Test if we have triumph-related tables
    print("\n4. Checking for triumph/record tables...")
    triumph_tables = [t for t in tables if 'record' in t.lower() or 'triumph' in t.lower() or 'collectible' in t.lower()]
    if triumph_tables:
        print("SUCCESS: Found triumph-related tables:")
        for table in triumph_tables:
            print(f"  - {table}")
    else:
        print("ERROR: No triumph-related tables found")
    
    # Test if we have stat/socket tables
    print("\n5. Checking for stat/socket tables...")
    system_tables = [t for t in tables if any(keyword in t.lower() for keyword in ['stat', 'socket', 'perk', 'talent'])]
    if system_tables:
        print("SUCCESS: Found system tables:")
        for table in system_tables:
            print(f"  - {table}")
    else:
        print("ERROR: No system tables found")
    
    print(f"\n=== TEST COMPLETE ===")
    print(f"Total definition tables: {len(tables)}")
    print(f"Total flattened records: {stats.get('total_records', 0):,}")
    
    return True

if __name__ == "__main__":
    test_enhanced_manifest()