"""
Main application entry point for the Destiny API Tools backend.
"""

import os
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
        print(f"Server running at: https://localhost:5001")
    else:
        print("Certificates not found, running HTTP server")
        print(f"Server running at: http://localhost:5001")
    
    app.run(debug=True, host='0.0.0.0', port=5001, ssl_context=ssl_context)