"""
Main application entry point for the Destiny API Tools backend.
"""

import os
from app import create_app

# Get configuration from environment or default to development
config_name = os.getenv('FLASK_ENV') or 'development'
app = create_app(config_name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)