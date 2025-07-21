#!/usr/bin/env python3
"""
Setup script for Destiny API Tools backend dependencies.
Installs required packages and sets up the development environment.
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, cwd=None):
    """Run a command and return the result."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            capture_output=True,
            text=True,
            cwd=cwd
        )
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr

def main():
    """Main setup function."""
    print("🚀 Setting up Destiny API Tools backend...")
    
    # Get the backend directory
    backend_dir = Path(__file__).parent / "backend"
    
    if not backend_dir.exists():
        print("❌ Backend directory not found!")
        sys.exit(1)
    
    # Check if we're in a virtual environment
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("⚠️  Warning: Not running in a virtual environment!")
        print("   Consider creating a virtual environment first:")
        print("   python -m venv backend/venv")
        print("   source backend/venv/bin/activate  # On Windows: backend\\venv\\Scripts\\activate")
        
        response = input("Continue anyway? (y/N): ")
        if response.lower() != 'y':
            print("Setup cancelled.")
            sys.exit(0)
    
    # Install requirements
    print("📦 Installing Python dependencies...")
    success, output = run_command("pip install -r requirements.txt", cwd=backend_dir)
    
    if not success:
        print(f"❌ Failed to install dependencies: {output}")
        sys.exit(1)
    
    print("✅ Dependencies installed successfully!")
    
    # Check for .env file
    env_file = backend_dir / ".env"
    env_example = backend_dir / ".env.example"
    
    if not env_file.exists():
        print("⚙️  Setting up environment configuration...")
        
        if env_example.exists():
            # Copy example file
            import shutil
            shutil.copy(env_example, env_file)
            print("✅ Created .env file from .env.example")
        else:
            # Create basic .env file
            env_content = """# Destiny API Tools Environment Configuration
# Get your API credentials from https://www.bungie.net/en/Application

# Required: Bungie API Credentials
BUNGIE_API_KEY=your_api_key_here
BUNGIE_CLIENT_ID=your_client_id_here
BUNGIE_CLIENT_SECRET=your_client_secret_here

# Optional: Application Configuration
FLASK_ENV=development
SECRET_KEY=your_secret_key_here

# Optional: Database Configuration
DATABASE_URL=sqlite:///destiny_tools.db

# Optional: Cache Configuration
CACHE_TYPE=simple
REDIS_URL=redis://localhost:6379/0
"""
            
            with open(env_file, 'w') as f:
                f.write(env_content)
            
            print("✅ Created basic .env file")
        
        print("🔧 Please edit the .env file and add your Bungie API credentials:")
        print(f"   {env_file}")
        print("   Get credentials from: https://www.bungie.net/en/Application")
    else:
        print("✅ Environment file already exists")
    
    # Create necessary directories
    directories = [
        backend_dir / "logs",
        backend_dir / "data",
        backend_dir / "temp"
    ]
    
    for directory in directories:
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)
            print(f"✅ Created directory: {directory.name}/")
    
    # Test the installation
    print("🧪 Testing installation...")
    
    test_script = """
import sys
sys.path.insert(0, '.')

try:
    # Test basic imports
    import flask
    import requests
    import schedule
    import psutil
    
    # Test app imports
    from app.config import config
    from app.utils.response import APIResponse
    
    print("✅ All imports successful!")
    print(f"✅ Flask version: {flask.__version__}")
    print(f"✅ Python version: {sys.version}")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"⚠️  Warning: {e}")
"""
    
    success, output = run_command(f"python -c \"{test_script}\"", cwd=backend_dir)
    
    if success:
        print(output.strip())
        print("\n🎉 Setup completed successfully!")
        print("\nNext steps:")
        print("1. Edit backend/.env with your Bungie API credentials")
        print("2. Run the backend: cd backend && python app.py")
        print("3. Set up the frontend: cd frontend && npm install && npm start")
    else:
        print(f"⚠️  Setup completed with warnings: {output}")
        print("\nYou may need to:")
        print("1. Check your Python version (3.8+ required)")
        print("2. Install missing system dependencies")
        print("3. Check the error messages above")

if __name__ == "__main__":
    main()