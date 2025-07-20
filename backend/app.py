"""
Main application entry point for the Destiny API Tools backend.
"""

import os
from app import create_app
from app.config import Config

# Create app with Config class
app = create_app(Config)

if __name__ == '__main__':
    # HTTPS configuration for local development
    ssl_context = None
    if os.path.exists('certs/localhost+2.pem') and os.path.exists('certs/localhost+2-key.pem'):
        ssl_context = ('certs/localhost+2.pem', 'certs/localhost+2-key.pem')
    
    port = 5000 if ssl_context is None else 5001
    app.run(debug=True, host='0.0.0.0', port=port, ssl_context=ssl_context)