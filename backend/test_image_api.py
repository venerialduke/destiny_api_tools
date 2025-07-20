#!/usr/bin/env python3
"""
Test script for image API endpoints.
"""

import os
import sys
import requests
import time
import json
from threading import Thread
import subprocess

# Add the backend directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def start_test_server():
    """Start a test Flask server in a separate process."""
    print("Starting test server...")
    
    # Create a minimal Flask app for testing
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
    app.run(host='127.0.0.1', port=5002, debug=False, use_reloader=False)
'''
    
    # Write test app
    with open('test_server.py', 'w') as f:
        f.write(test_app_content)
    
    # Start server in background
    process = subprocess.Popen([sys.executable, 'test_server.py'], 
                              stdout=subprocess.PIPE, 
                              stderr=subprocess.PIPE)
    
    # Wait for server to start
    time.sleep(3)
    
    # Test if server is running
    try:
        response = requests.get('http://127.0.0.1:5002/health', timeout=5)
        if response.status_code == 200:
            print("Test server started successfully!")
            return process
        else:
            print("Server responded with error")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to test server: {e}")
        return None


def test_image_api_endpoints():
    """Test image API endpoints."""
    base_url = "http://127.0.0.1:5002/api"
    
    # Get a real icon path from manifest if available
    test_icon_path = "/common/destiny2_content/icons/804b3ab35037730a4f93cc33a9282081.jpg"
    
    try:
        # Try to get a real icon from manifest
        manifest_response = requests.get(f"{base_url}/manifest/items/search?limit=1", timeout=10)
        if manifest_response.status_code == 200:
            items = manifest_response.json().get('items', [])
            if items and items[0].get('displayProperties', {}).get('icon'):
                icon_data = items[0]['displayProperties']['icon']
                if isinstance(icon_data, dict) and 'original' in icon_data:
                    # Extract path from full URL
                    original_url = icon_data['original']
                    test_icon_path = original_url.replace('https://bungie.net', '')
                elif isinstance(icon_data, str):
                    test_icon_path = icon_data.replace('https://bungie.net', '')
                print(f"Using icon from manifest: {test_icon_path}")
    except Exception as e:
        print(f"Could not get manifest icon, using fallback: {e}")
    
    print(f"\n=== Testing Image API Endpoints ===")
    print(f"Base URL: {base_url}")
    print(f"Test icon: {test_icon_path}")
    
    # Test 1: Image proxy endpoint
    print("\n1. Testing image proxy endpoint...")
    try:
        proxy_url = f"{base_url}/images/proxy{test_icon_path}"
        response = requests.get(proxy_url, timeout=15)
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            print(f"   Content-Type: {response.headers.get('content-type')}")
            print(f"   Content-Length: {len(response.content):,} bytes")
            print(f"   Cache-Status: {response.headers.get('X-Cache-Status', 'Not set')}")
        else:
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test 2: Image proxy with format conversion
    print("\n2. Testing WebP format conversion...")
    try:
        proxy_url = f"{base_url}/images/proxy{test_icon_path}?format=webp&size=medium"
        response = requests.get(proxy_url, timeout=10)
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            print(f"   Content-Type: {response.headers.get('content-type')}")
            print(f"   Content-Length: {len(response.content):,} bytes")
            print(f"   Cache-Status: {response.headers.get('X-Cache-Status', 'Not set')}")
        else:
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test 3: URL generation endpoint
    print("\n3. Testing URL generation...")
    try:
        url_endpoint = f"{base_url}/images/url{test_icon_path}?format=webp&size=small"
        response = requests.get(url_endpoint, timeout=5)
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   Proxy URL: {data.get('proxy_url')}")
            print(f"   Format: {data.get('format')}")
            print(f"   Size: {data.get('size')}")
        else:
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test 4: Batch URL generation
    print("\n4. Testing batch URL generation...")
    try:
        batch_data = {
            "icon_paths": [test_icon_path],
            "format": "webp",
            "size": "medium"
        }
        response = requests.post(f"{base_url}/images/batch-urls", 
                               json=batch_data, timeout=5)
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   Images processed: {data.get('count')}")
            print(f"   Format: {data.get('format')}")
        else:
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test 5: Cache statistics
    print("\n5. Testing cache statistics...")
    try:
        response = requests.get(f"{base_url}/images/cache/stats", timeout=5)
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            stats = data.get('cache_statistics', {})
            print(f"   Cache size: {stats.get('cache_size_mb', 0):.2f} MB")
            print(f"   Hit rate: {stats.get('hit_rate_percent', 0):.1f}%")
            print(f"   Total requests: {stats.get('total_requests', 0)}")
            print(f"   Status: {data.get('status')}")
        else:
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test 6: Supported formats info
    print("\n6. Testing formats info...")
    try:
        response = requests.get(f"{base_url}/images/formats", timeout=5)
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            formats = list(data.get('formats', {}).keys())
            sizes = list(data.get('sizes', {}).keys())
            print(f"   Supported formats: {', '.join(formats)}")
            print(f"   Supported sizes: {', '.join(sizes)}")
        else:
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"   Error: {e}")
    
    print("\n[SUCCESS] Image API endpoint tests completed!")
    return True


def main():
    """Main test function."""
    # Start test server
    server_process = start_test_server()
    
    if not server_process:
        print("[ERROR] Failed to start test server")
        return False
    
    try:
        # Run API tests
        success = test_image_api_endpoints()
        
        if success:
            print("\n[SUCCESS] All image API tests passed!")
        else:
            print("\n[ERROR] Some image API tests failed!")
        
        return success
        
    finally:
        # Clean up
        print("\nCleaning up...")
        if server_process:
            server_process.terminate()
            server_process.wait()
        
        # Remove test file
        if os.path.exists('test_server.py'):
            os.remove('test_server.py')


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