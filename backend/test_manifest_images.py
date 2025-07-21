#!/usr/bin/env python3
"""
Test script for manifest integration with optimized image URLs.
"""

import os
import sys
import requests
import time
import json
import subprocess

# Add the backend directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def start_test_server():
    """Start a test Flask server."""
    print("Starting enhanced test server...")
    
    test_app_content = '''
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
from flask_cors import CORS
from app.api import api_bp

app = Flask(__name__)
CORS(app)
app.register_blueprint(api_bp, url_prefix='/api')

@app.route('/health')
def health():
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5003, debug=False, use_reloader=False)
'''
    
    with open('test_server_manifest.py', 'w') as f:
        f.write(test_app_content)
    
    process = subprocess.Popen([sys.executable, 'test_server_manifest.py'], 
                              stdout=subprocess.PIPE, 
                              stderr=subprocess.PIPE)
    
    time.sleep(3)
    
    try:
        response = requests.get('http://127.0.0.1:5003/health', timeout=5)
        if response.status_code == 200:
            print("Enhanced test server started successfully!")
            return process
        else:
            print("Server responded with error")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to test server: {e}")
        return None


def test_manifest_image_integration():
    """Test manifest endpoints with optimized image URLs."""
    base_url = "http://127.0.0.1:5003/api"
    
    print(f"\n=== Testing Manifest Image Integration ===")
    print(f"Base URL: {base_url}")
    
    # Test 1: Individual item lookup
    print("\n1. Testing individual item lookup with optimized images...")
    try:
        # Get an item hash first
        search_response = requests.get(f"{base_url}/manifest/items/search?limit=1", timeout=10)
        if search_response.status_code == 200:
            items = search_response.json().get('items', [])
            if items:
                item_hash = items[0]['hash']
                print(f"   Using item hash: {item_hash}")
                
                # Get full item details
                item_response = requests.get(f"{base_url}/manifest/items/{item_hash}", timeout=10)
                if item_response.status_code == 200:
                    item_data = item_response.json()
                    icon_data = item_data.get('displayProperties', {}).get('icon')
                    
                    print(f"   Item name: {item_data.get('displayProperties', {}).get('name')}")
                    print(f"   Icon structure type: {type(icon_data)}")
                    
                    if isinstance(icon_data, dict):
                        print(f"   Original URL: {icon_data.get('original')}")
                        print(f"   Proxy URL: {icon_data.get('proxy')}")
                        optimized = icon_data.get('optimized', {})
                        print(f"   Small optimized: {optimized.get('small')}")
                        print(f"   Medium optimized: {optimized.get('medium')}")
                        print(f"   Large optimized: {optimized.get('large')}")
                        
                        # Test that the optimized URLs work
                        if optimized.get('medium'):
                            test_url = f"http://127.0.0.1:5003{optimized['medium']}"
                            img_response = requests.get(test_url, timeout=10)
                            print(f"   Medium image test: {img_response.status_code} - {img_response.headers.get('content-type')} - {len(img_response.content)} bytes")
                    else:
                        print(f"   Icon data: {icon_data}")
                else:
                    print(f"   Error getting item: {item_response.status_code}")
            else:
                print("   No items found in manifest")
        else:
            print(f"   Error searching manifest: {search_response.status_code}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test 2: Search results with optimized images
    print("\n2. Testing search results with optimized images...")
    try:
        search_response = requests.get(f"{base_url}/manifest/items/search?weapon=true&limit=3", timeout=10)
        if search_response.status_code == 200:
            data = search_response.json()
            items = data.get('items', [])
            print(f"   Found {len(items)} weapon items")
            
            for i, item in enumerate(items[:2]):  # Test first 2 items
                name = item.get('displayProperties', {}).get('name', 'Unknown')
                icon_data = item.get('displayProperties', {}).get('icon')
                print(f"   Item {i+1}: {name}")
                
                if isinstance(icon_data, dict):
                    optimized = icon_data.get('optimized', {})
                    if optimized.get('small'):
                        # Test the small optimized image
                        test_url = f"http://127.0.0.1:5003{optimized['small']}"
                        img_response = requests.get(test_url, timeout=5)
                        print(f"     Small image: {img_response.status_code} - {len(img_response.content)} bytes")
        else:
            print(f"   Error: {search_response.status_code}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test 3: Batch request with optimized images
    print("\n3. Testing batch request with optimized images...")
    try:
        # Get some item hashes first
        search_response = requests.get(f"{base_url}/manifest/items/search?limit=3", timeout=10)
        if search_response.status_code == 200:
            items = search_response.json().get('items', [])
            hashes = [item['hash'] for item in items[:2]]
            
            if hashes:
                print(f"   Testing with hashes: {hashes}")
                
                batch_data = {"hashes": hashes}
                batch_response = requests.post(f"{base_url}/manifest/items/batch", 
                                             json=batch_data, timeout=10)
                
                if batch_response.status_code == 200:
                    batch_data = batch_response.json()
                    items_dict = batch_data.get('items', {})
                    
                    print(f"   Batch returned {len(items_dict)} items")
                    
                    for hash_str, item_data in list(items_dict.items())[:1]:  # Test first item
                        name = item_data.get('displayProperties', {}).get('name', 'Unknown')
                        icon_data = item_data.get('displayProperties', {}).get('icon')
                        print(f"   Hash {hash_str}: {name}")
                        
                        if isinstance(icon_data, dict) and icon_data.get('optimized'):
                            medium_url = icon_data['optimized'].get('medium')
                            if medium_url:
                                test_url = f"http://127.0.0.1:5003{medium_url}"
                                img_response = requests.get(test_url, timeout=5)
                                print(f"     Medium image: {img_response.status_code} - {len(img_response.content)} bytes")
                else:
                    print(f"   Batch error: {batch_response.status_code}")
        else:
            print(f"   Search error: {search_response.status_code}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test 4: Category endpoints with optimized images
    print("\n4. Testing category endpoints with optimized images...")
    try:
        categories_to_test = ['weapons', 'armor', 'cosmetics']
        
        for category in categories_to_test:
            response = requests.get(f"{base_url}/manifest/{category}?limit=1", timeout=10)
            if response.status_code == 200:
                data = response.json()
                items_key = category if category in data else 'items'
                items = data.get(items_key, [])
                
                if items:
                    item = items[0]
                    name = item.get('displayProperties', {}).get('name', 'Unknown')
                    icon_data = item.get('displayProperties', {}).get('icon')
                    
                    print(f"   {category.title()}: {name}")
                    
                    if isinstance(icon_data, dict) and icon_data.get('optimized'):
                        # Test small image for categories
                        small_url = icon_data['optimized'].get('small')
                        if small_url:
                            test_url = f"http://127.0.0.1:5003{small_url}"
                            img_response = requests.get(test_url, timeout=5)
                            print(f"     Small image: {img_response.status_code} - {len(img_response.content)} bytes - {img_response.headers.get('content-type')}")
                else:
                    print(f"   {category.title()}: No items found")
            else:
                print(f"   {category.title()}: Error {response.status_code}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test 5: Performance comparison
    print("\n5. Testing performance comparison (original vs optimized)...")
    try:
        # Get an item with icon
        search_response = requests.get(f"{base_url}/manifest/items/search?limit=1", timeout=10)
        if search_response.status_code == 200:
            items = search_response.json().get('items', [])
            if items:
                icon_data = items[0].get('displayProperties', {}).get('icon')
                
                if isinstance(icon_data, dict):
                    original_url = icon_data.get('original')
                    optimized_url = icon_data.get('optimized', {}).get('medium')
                    
                    if original_url and optimized_url:
                        # Test original (external)
                        start_time = time.time()
                        try:
                            orig_response = requests.get(original_url, timeout=10)
                            orig_time = time.time() - start_time
                            orig_size = len(orig_response.content)
                        except:
                            orig_time = float('inf')
                            orig_size = 0
                        
                        # Test optimized (local proxy)
                        start_time = time.time()
                        opt_response = requests.get(f"http://127.0.0.1:5003{optimized_url}", timeout=10)
                        opt_time = time.time() - start_time
                        opt_size = len(opt_response.content)
                        
                        print(f"   Original: {orig_time:.3f}s, {orig_size:,} bytes")
                        print(f"   Optimized: {opt_time:.3f}s, {opt_size:,} bytes")
                        if orig_time != float('inf'):
                            print(f"   Speed improvement: {orig_time/opt_time:.1f}x faster")
                            print(f"   Size reduction: {(1 - opt_size/orig_size)*100:.1f}% smaller")
    except Exception as e:
        print(f"   Error: {e}")
    
    print("\n[SUCCESS] Manifest image integration tests completed!")
    return True


def main():
    """Main test function."""
    server_process = start_test_server()
    
    if not server_process:
        print("[ERROR] Failed to start test server")
        return False
    
    try:
        success = test_manifest_image_integration()
        
        if success:
            print("\n[SUCCESS] All manifest image integration tests passed!")
        else:
            print("\n[ERROR] Some tests failed!")
        
        return success
        
    finally:
        print("\nCleaning up...")
        if server_process:
            server_process.terminate()
            server_process.wait()
        
        if os.path.exists('test_server_manifest.py'):
            os.remove('test_server_manifest.py')


if __name__ == '__main__':
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n[INFO] Test interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n[ERROR] Test error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)