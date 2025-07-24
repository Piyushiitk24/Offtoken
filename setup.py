#!/usr/bin/env python3
"""
TokenForge - Setup and Launch Script
Professional setup with automatic dependency management
"""

import subprocess
import sys
import os
import webbrowser
from pathlib import Path

def run_command(cmd, description=""):
    """Run a command and handle errors gracefully"""
    print(f"🔄 {description}")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        if result.stdout:
            print(f"   ✅ Success")
        return True
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Error: {e.stderr.strip()}")
        return False

def install_dependencies():
    """Install Python dependencies"""
    print("� Installing dependencies...")
    
    # Upgrade pip
    if not run_command(f"{sys.executable} -m pip install --upgrade pip", "Upgrading pip"):
        return False
    
    # Install requirements
    if not run_command(f"{sys.executable} -m pip install -r requirements.txt", "Installing packages"):
        return False
    
    return True

def launch_app():
    """Launch the TokenForge application"""
    print("\n✅ Setup complete!")
    print("🌐 Starting TokenForge...")
    print("📱 Your browser will open automatically")
    print("\nPress Ctrl+C to stop the application\n")
    
    try:
        # Open browser after a short delay
        import threading
        import time
        
        def open_browser():
            time.sleep(2)
            webbrowser.open('http://localhost:8501')
        
        threading.Thread(target=open_browser, daemon=True).start()
        
        # Launch Streamlit
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py", "--server.headless=true"], check=True)
        
    except KeyboardInterrupt:
        print("\n� TokenForge stopped")
    except Exception as e:
        print(f"❌ Error launching TokenForge: {e}")
        sys.exit(1)

def main():
    print("🚀 TokenForge Setup")
    print("=" * 30)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ required")
        sys.exit(1)
    
    print(f"✅ Python {sys.version.split()[0]} detected")
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Dependency installation failed")
        sys.exit(1)
    
    # Launch application
    launch_app()

if __name__ == "__main__":
    main()
