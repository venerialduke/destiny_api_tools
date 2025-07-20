"""
Main application entry point for the Destiny API Tools backend.
"""

import os
from app import create_app
from app.config import Config

# Create app with Config class
app = create_app(Config)

if __name__ == '__main__':
    # Run on HTTP for demo purposes (avoid certificate issues)
    app.run(debug=True, host='0.0.0.0', port=5001)