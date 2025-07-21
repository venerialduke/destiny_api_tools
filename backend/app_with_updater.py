#!/usr/bin/env python3
"""
Enhanced Flask application with automatic manifest updates.
"""

import os
import sys
import logging
from flask import Flask
from flask_cors import CORS

# Add the backend directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.config import Config
from app.api import api_bp
from app.services.startup_service import get_startup_service

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('app.log') if os.path.exists('.') else logging.NullHandler()
    ]
)

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Enable CORS
    CORS(app)
    
    # Register API blueprint
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # Add basic health check endpoint
    @app.route('/health')
    def health_check():
        return {'status': 'healthy', 'message': 'Destiny API Tools is running'}
    
    @app.route('/')
    def index():
        return {
            'message': 'Destiny API Tools - Enhanced with Automatic Updates',
            'version': '2.0.0',
            'features': [
                'Automatic manifest updates',
                'Full-text search',
                '11 item categories', 
                'Performance monitoring',
                'Health checks',
                'Background services'
            ],
            'endpoints': {
                'manifest': '/api/manifest/',
                'updater': '/api/updater/',
                'health': '/health'
            }
        }
    
    return app

def main():
    """Main application entry point."""
    app = create_app()
    
    # Initialize application services
    startup_service = get_startup_service()
    
    try:
        # Initialize with auto-start updater
        startup_service.initialize_application(auto_start_updater=True)
        
        # Run the Flask application
        port = int(os.environ.get('PORT', 5001))
        debug = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
        
        print(f"\n🚀 Starting Destiny API Tools Enhanced Server")
        print(f"📍 Server: https://localhost:{port}")
        print(f"📊 Health: https://localhost:{port}/health")
        print(f"🔄 Updater: https://localhost:{port}/api/updater/status")
        print(f"📚 Manifest: https://localhost:{port}/api/manifest/status")
        print(f"🎯 Dashboard: https://localhost:{port}/api/updater/dashboard")
        print(f"\n✨ Features:")
        print(f"   • Automatic manifest updates every 6 hours")
        print(f"   • Real-time health monitoring")
        print(f"   • Full-text search with FTS5")
        print(f"   • 13 API endpoints for manifest access")
        print(f"   • Background error recovery")
        print(f"   • Performance metrics")
        print(f"\n🔧 Management:")
        print(f"   • POST /api/updater/start - Start background updates")
        print(f"   • POST /api/updater/stop - Stop background updates")
        print(f"   • POST /api/updater/force-update - Force immediate update")
        print(f"   • GET /api/updater/system-health - Complete system status")
        print(f"\n")
        
        app.run(
            host='0.0.0.0',
            port=port,
            debug=debug,
            ssl_context='adhoc' if not debug else None
        )
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down gracefully...")
        startup_service.shutdown_application()
        print("✅ Shutdown complete")
    except Exception as e:
        print(f"\n❌ Application error: {e}")
        startup_service.shutdown_application()
        sys.exit(1)

if __name__ == '__main__':
    main()