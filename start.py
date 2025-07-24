#!/usr/bin/env python3
"""
TokenForge Quick Start
Ultimate one-command launcher for all TokenForge features
"""

import os
import sys
import subprocess
import time
from pathlib import Path

def main():
    """Main launcher"""
    print("""
    ✨✨✨ TOKENFORGE - PROFESSIONAL TOKEN COUNTER ✨✨✨
    
    🌈 Beautiful PRIDE-Themed UI • 🎯 Authentic Tokenizers • 🔒 Privacy First
    
    Choose your experience:
    
    1. 🎨 Launch Beautiful UI (Streamlit App)
    2. 🌍 View Landing Page (GitHub Pages)  
    3. 🚀 Complete Demo (All Features)
    4. 🐳 Docker Deployment
    5. 🔒 Security Check
    6. 📖 View Documentation
    """)
    
    try:
        choice = input("👉 Enter your choice (1-6): ").strip()
        
        if choice == "1":
            print("\n🎨 Launching TokenForge with beautiful PRIDE-themed UI...")
            print("🌈 Features: Gradient backgrounds, smooth animations, responsive design")
            os.system("source .venv/bin/activate && streamlit run app.py")
            
        elif choice == "2":
            print("\n🌍 Opening GitHub Pages landing site...")
            subprocess.Popen(["python3", "preview_pages.py"])
            
        elif choice == "3":
            print("\n🚀 Starting complete feature demonstration...")
            os.system("python3 demo_tokenforge.py")
            
        elif choice == "4":
            print("\n🐳 Docker deployment options:")
            print("   • docker-compose up -d (recommended)")
            print("   • docker build -t tokenforge . && docker run -p 8501:8501 tokenforge")
            
        elif choice == "5":
            print("\n🔒 Running security check...")
            os.system("python3 security_scan.py")
            
        elif choice == "6":
            print("\n📖 Documentation available:")
            print("   • README.md - Main documentation")
            print("   • DEPLOYMENT.md - Complete deployment guide")
            print("   • SECURITY.md - Security policy")
            
        else:
            print("❌ Invalid choice")
            
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")

if __name__ == "__main__":
    main()
