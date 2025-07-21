#!/usr/bin/env python3
"""
Direct test of image proxy endpoint to debug 500 errors.
"""

import requests
import time

def test_image_endpoints():
    base_url = "http://localhost:5001"
    
    # Test different image URLs to see which ones work
    test_paths = [
        "/common/destiny2_content/icons/804b3ab35037730a4f93cc33a9282081.jpg",
        "/common/destiny2_content/icons/e0190b75e472f6e552cffe8e4dd29fe0.jpg",
        "/common/destiny2_content/icons/6e948a6e8f28ae201b9895c70dfa1c6a.jpg"
    ]
    
    for path in test_paths:
        print(f"\nTesting: {path}")
        
        # Test various formats and sizes
        test_urls = [
            f"{base_url}/api/images/proxy{path}",
            f"{base_url}/api/images/proxy{path}?format=webp",
            f"{base_url}/api/images/proxy{path}?format=webp&size=small",
            f"{base_url}/api/images/proxy{path}?format=jpg&size=small"
        ]
        
        for url in test_urls:
            try:
                print(f"  Testing: {url}")
                response = requests.get(url, timeout=10)
                print(f"    Status: {response.status_code}")
                
                if response.status_code == 200:
                    print(f"    Content-Type: {response.headers.get('content-type')}")
                    print(f"    Size: {len(response.content)} bytes")
                    print(f"    Cache Status: {response.headers.get('X-Cache-Status', 'Not set')}")
                else:
                    print(f"    Error: {response.text[:200]}")
                    
            except Exception as e:
                print(f"    Exception: {e}")

if __name__ == "__main__":
    print("Testing image proxy endpoints...")
    test_image_endpoints()
    print("\nTest complete!")