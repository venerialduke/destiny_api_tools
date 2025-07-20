#!/usr/bin/env python3
"""
Test script for image service functionality.
"""

import os
import sys
import time
import requests

# Add the backend directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.services.image_service import get_image_service


def test_image_service():
    """Test the image service functionality."""
    print("=== Testing Image Service ===\n")
    
    # Initialize image service
    image_service = get_image_service()
    
    # Test icon path (use a known Destiny icon)
    # This is a generic placeholder - we'll test with a real icon from manifest
    test_icon_path = None
    
    # Try to get a real icon from manifest
    try:
        from app.services.database_service import DatabaseService
        db_path = os.path.join('data', 'manifest.db')
        if os.path.exists(db_path):
            db_service = DatabaseService(db_path)
            results = db_service.search_items(limit=1)
            if results['items']:
                test_icon_path = results['items'][0]['icon']
                print(f"Using real icon from manifest: {test_icon_path}")
    except Exception as e:
        print(f"Could not get icon from manifest: {e}")
    
    # Fallback to a known Bungie icon (Gjallarhorn)
    if not test_icon_path:
        test_icon_path = "/common/destiny2_content/icons/3460c5ac92e41e92d3ca7fdb3edda46e.jpg"
    
    print(f"Testing with icon path: {test_icon_path}")
    
    # Test 1: Get image URL generation
    print("\n1. Testing URL generation...")
    proxy_url = image_service.get_image_url(test_icon_path, 'webp', 'medium')
    print(f"   Generated proxy URL: {proxy_url}")
    
    # Test 2: Check cache (should be empty initially)
    print("\n2. Testing cache lookup (should be empty)...")
    cached_result = image_service.get_cached_image(test_icon_path, 'webp', 'medium')
    print(f"   Cache result: {'HIT' if cached_result else 'MISS'}")
    
    # Test 3: Download and cache image
    print("\n3. Testing download and caching...")
    start_time = time.time()
    download_result = image_service.download_and_cache_image(test_icon_path, 'webp', 'medium')
    download_time = time.time() - start_time
    
    if download_result:
        image_data, content_type = download_result
        print(f"   Download successful!")
        print(f"   Content type: {content_type}")
        print(f"   Image size: {len(image_data):,} bytes")
        print(f"   Download time: {download_time:.2f}s")
    else:
        print("   Download failed!")
        return False
    
    # Test 4: Check cache again (should be HIT now)
    print("\n4. Testing cache lookup again (should be HIT)...")
    start_time = time.time()
    cached_result = image_service.get_cached_image(test_icon_path, 'webp', 'medium')
    cache_time = time.time() - start_time
    
    if cached_result:
        cached_data, cached_content_type, cached_time_stamp = cached_result
        print(f"   Cache HIT!")
        print(f"   Cached size: {len(cached_data):,} bytes")
        print(f"   Cache lookup time: {cache_time:.4f}s")
        print(f"   Cached at: {cached_time_stamp}")
        print(f"   Speed improvement: {download_time/cache_time:.1f}x faster")
    else:
        print("   Cache MISS (unexpected!)")
        return False
    
    # Test 5: Test different formats
    print("\n5. Testing different formats...")
    formats_to_test = ['original', 'jpg', 'png']
    
    for fmt in formats_to_test:
        print(f"   Testing format: {fmt}")
        result = image_service.download_and_cache_image(test_icon_path, fmt, 'small')
        if result:
            data, content_type = result
            print(f"     Success: {len(data):,} bytes, {content_type}")
        else:
            print(f"     Failed for format: {fmt}")
    
    # Test 6: Cache statistics
    print("\n6. Testing cache statistics...")
    stats = image_service.get_cache_stats()
    print(f"   Cache size: {stats['cache_size_mb']:.2f} MB")
    print(f"   Hit rate: {stats['hit_rate_percent']:.1f}%")
    print(f"   Total requests: {stats['total_requests']}")
    print(f"   Downloads: {stats['downloads']}")
    print(f"   Errors: {stats['errors']}")
    
    print("\n[SUCCESS] Image service test completed successfully!")
    return True


if __name__ == '__main__':
    try:
        success = test_image_service()
        if success:
            print("\n[SUCCESS] All image service tests passed!")
        else:
            print("\n[ERROR] Some tests failed!")
            sys.exit(1)
    except Exception as e:
        print(f"\n[ERROR] Test error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)