"""
Main application entry point for the Destiny API Tools backend.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file FIRST
load_dotenv()

# Debug: Check if environment variables are loaded
print(f"ENV: BUNGIE_API_KEY: {os.environ.get('BUNGIE_API_KEY', 'NOT SET')}")
print(f"ENV: BUNGIE_CLIENT_ID: {os.environ.get('BUNGIE_CLIENT_ID', 'NOT SET')}")
print(f"ENV: BUNGIE_CLIENT_SECRET: {os.environ.get('BUNGIE_CLIENT_SECRET', 'NOT SET')[:10]}...")

# Import after loading .env to ensure config reads the right values
from app import create_app
from app.config import Config

# Create app with Config class
app = create_app(Config)

if __name__ == '__main__':
    # SSL context for local HTTPS development
    ssl_context = None
    cert_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'certs')
    cert_file = os.path.join(cert_dir, 'localhost+2.pem')
    key_file = os.path.join(cert_dir, 'localhost+2-key.pem')
    
    # Use HTTPS with existing mkcert certificates if they exist
    if os.path.exists(cert_file) and os.path.exists(key_file):
        ssl_context = (cert_file, key_file)
        print(f"Starting server with HTTPS using certificates:")
        print(f"  Cert: {cert_file}")
        print(f"  Key:  {key_file}")
        print(f"Server running at: https://localhost:5000")
    else:
        print("Certificates not found, running HTTP server")
        print(f"Server running at: http://localhost:5000")
    
    # Print registered routes for debugging
    print("\nRegistered API Routes:")
    for rule in app.url_map.iter_rules():
        if rule.rule.startswith('/api'):
            methods = ','.join(sorted(rule.methods - {'HEAD', 'OPTIONS'}))
            print(f"  {methods:8} {rule.rule}")
    
    print("\nAuth endpoints should be available at:")
    print("  GET      /api/auth/login")
    print("  POST     /api/auth/callback") 
    print("  POST     /api/auth/refresh")
    print("  POST     /api/auth/logout")
    print("\n" + "="*50)
    
    app.run(debug=True, host='0.0.0.0', port=5000, ssl_context=ssl_context)