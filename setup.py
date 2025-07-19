#!/usr/bin/env python3
"""
Token Counter Pro - Setup and Launch Script
Handles all dependencies and launches the application
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(cmd, description=""):
    """Run a command and handle errors"""
    print(f"🔄 {description}")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        if result.stdout:
            print(f"   ✅ {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Error: {e.stderr.strip()}")
        return False

def check_system_deps():
    """Check and install system dependencies"""
    print("🔍 Checking system dependencies...")
    
    # Check Homebrew
    if not run_command("which brew", "Checking Homebrew"):
        print("❌ Homebrew not found. Install from https://brew.sh")
        return False
    
    # Check and install Tesseract
    if not run_command("which tesseract", "Checking Tesseract"):
        if not run_command("brew install tesseract", "Installing Tesseract"):
            return False
    
    # Check and install Poppler
    if not run_command("which pdftoppm", "Checking Poppler"):
        if not run_command("brew install poppler", "Installing Poppler"):
            return False
    
    return True

def setup_python_env():
    """Setup Python virtual environment"""
    print("🐍 Setting up Python environment...")
    
    # Create virtual environment
    if not Path(".venv").exists():
        if not run_command("python3 -m venv .venv", "Creating virtual environment"):
            return False
    
    # Install dependencies
    activate_cmd = "source .venv/bin/activate && "
    
    if not run_command(f"{activate_cmd}pip install --upgrade pip", "Upgrading pip"):
        return False
    
    if not run_command(f"{activate_cmd}pip install -r requirements.txt", "Installing dependencies"):
        return False
    
    return True

def main():
    print("🚀 Token Counter Pro Setup")
    print("=" * 40)
    
    # Check system dependencies
    if not check_system_deps():
        print("❌ System setup failed")
        sys.exit(1)
    
    # Setup Python environment
    if not setup_python_env():
        print("❌ Python setup failed")
        sys.exit(1)
    
    print("\n✅ Setup complete!")
    print("🌐 Starting Token Counter Pro...")
    print("📱 Open http://localhost:8501 in your browser")
    print("\nPress Ctrl+C to stop the application\n")
    
    # Launch the application
    activate_cmd = "source .venv/bin/activate && "
    try:
        subprocess.run(f"{activate_cmd}streamlit run app.py", shell=True, check=True)
    except KeyboardInterrupt:
        print("\n👋 Application stopped")
    except Exception as e:
        print(f"❌ Error launching application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
