#!/usr/bin/env python3
"""
TokenForge Demo Script
Demonstrates all the beautiful new features and deployment options
"""

import os
import sys
import time
import webbrowser
import subprocess
from pathlib import Path

def print_banner():
    """Print a beautiful banner"""
    banner = """
    ✨ ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗███████╗ ██████╗ ██████╗  ████████╗
    ✨ ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║██╔════╝██╔═══██╗██╔══██╗ ██╔═════╝
    ✨    ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║█████╗  ██║   ██║██████╔╝ ██║  ███╗
    ✨    ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗ ██║   ██║
    ✨    ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║██║     ╚██████╔╝██║  ██║ ╚██████╔╝
    ✨    ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝  ╚═╝  ╚═════╝ 
    
    🌈 Professional Token Counter with Beautiful PRIDE-Themed UI 🌈
    """
    print(banner)

def run_command(cmd, description, check=True):
    """Run a command with pretty output"""
    print(f"\n🔄 {description}...")
    print(f"   💻 Command: {cmd}")
    print("   " + "─" * 50)
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"   ✅ Success!")
            if result.stdout.strip():
                print(f"   📝 Output: {result.stdout.strip()[:200]}...")
        else:
            print(f"   ❌ Failed with code {result.returncode}")
            if result.stderr.strip():
                print(f"   🚨 Error: {result.stderr.strip()[:200]}...")
        
        return result.returncode == 0
    
    except Exception as e:
        print(f"   💥 Exception: {e}")
        return False

def demo_features():
    """Demonstrate all TokenForge features"""
    print("\n🎨 TOKENFORGE FEATURE DEMONSTRATION")
    print("=" * 60)
    
    features = [
        {
            "name": "🌈 Beautiful PRIDE-Themed UI",
            "description": "Stunning visual design with subtle PRIDE colors",
            "details": [
                "✨ Gradient hero sections with smooth animations",
                "🎨 Color-coded metrics with PRIDE accent colors", 
                "📱 Fully responsive design for all devices",
                "🌟 Smooth hover effects and transitions"
            ]
        },
        {
            "name": "🎯 Authentic Tokenizers",
            "description": "Real OpenAI tiktoken library for 100% accuracy",
            "details": [
                "🤖 GPT-4, GPT-3.5 Turbo, GPT-3 support",
                "📊 cl100k_base and p50k_base encodings",
                "⚡ Lightning-fast processing",
                "🎪 Same algorithms as OpenAI APIs"
            ]
        },
        {
            "name": "📄 Multi-Format Document Support",
            "description": "Process PDF, DOCX, and TXT files seamlessly",
            "details": [
                "📑 PDF text extraction with pdfplumber",
                "🔍 OCR support for scanned documents",
                "📝 DOCX and TXT file processing",
                "🖼️ Image-to-text conversion"
            ]
        },
        {
            "name": "💰 Smart Cost Estimation",
            "description": "Accurate API cost calculation with presets",
            "details": [
                "💸 Real-time cost calculation",
                "⚡ Quick preset buttons for popular models",
                "📈 Token efficiency analysis",
                "💡 Budget planning capabilities"
            ]
        },
        {
            "name": "📊 Advanced Analytics",
            "description": "Comprehensive token analysis and insights",
            "details": [
                "📏 Token-to-word ratios",
                "🔬 Detailed token breakdowns",
                "📈 Efficiency metrics",
                "🎯 First token previews"
            ]
        },
        {
            "name": "🔒 Privacy & Security",
            "description": "Enterprise-grade security with local processing",
            "details": [
                "🏠 100% local processing",
                "🚫 No data collection or transmission",
                "🔐 Pre-commit security hooks",
                "🛡️ Automated secret detection"
            ]
        },
        {
            "name": "🚀 Multiple Deployment Options",
            "description": "Deploy anywhere - local, cloud, or container",
            "details": [
                "🏠 Local development with one command",
                "☁️ Streamlit Cloud deployment",
                "🌍 GitHub Pages landing site",
                "🐳 Docker containerization"
            ]
        }
    ]
    
    for i, feature in enumerate(features, 1):
        print(f"\n{i}. {feature['name']}")
        print(f"   {feature['description']}")
        
        for detail in feature['details']:
            print(f"   {detail}")
        
        time.sleep(0.5)  # Small delay for dramatic effect

def show_deployment_options():
    """Show all deployment options"""
    print("\n🚀 DEPLOYMENT OPTIONS")
    print("=" * 40)
    
    deployments = [
        {
            "name": "🏠 Local Development",
            "command": "python3 setup.py",
            "description": "One-command setup and launch",
            "perfect_for": "Development, private documents, offline use"
        },
        {
            "name": "☁️ Streamlit Cloud", 
            "command": "# Fork → Connect → Deploy",
            "description": "Easy cloud deployment",
            "perfect_for": "Team sharing, public demos, easy access"
        },
        {
            "name": "🌍 GitHub Pages",
            "command": "python3 preview_pages.py",
            "description": "Beautiful landing page",
            "perfect_for": "Project showcase, documentation"
        },
        {
            "name": "🐳 Docker",
            "command": "docker-compose up -d",
            "description": "Containerized deployment",
            "perfect_for": "Production, scaling, cloud deployment"
        }
    ]
    
    for deployment in deployments:
        print(f"\n{deployment['name']}")
        print(f"   📝 {deployment['description']}")
        print(f"   💻 Command: {deployment['command']}")
        print(f"   ✅ Perfect for: {deployment['perfect_for']}")

def interactive_demo():
    """Interactive demonstration"""
    print("\n🎮 INTERACTIVE DEMO")
    print("=" * 30)
    
    options = [
        ("🎨 View Beautiful UI (Streamlit)", "streamlit"),
        ("🌍 View Landing Page (GitHub Pages)", "pages"),
        ("🧪 Run Security Tests", "security"),
        ("📊 Run Core Tests", "tests"),
        ("🐳 Build Docker Image", "docker"),
        ("📖 View Documentation", "docs"),
        ("❌ Exit Demo", "exit")
    ]
    
    while True:
        print("\n🌟 What would you like to see?")
        for i, (option, _) in enumerate(options, 1):
            print(f"   {i}. {option}")
        
        try:
            choice = input("\n👉 Enter your choice (1-7): ").strip()
            
            if not choice.isdigit() or int(choice) < 1 or int(choice) > len(options):
                print("❌ Invalid choice. Please try again.")
                continue
            
            selected = options[int(choice) - 1][1]
            
            if selected == "exit":
                print("\n👋 Thanks for exploring TokenForge!")
                break
            elif selected == "streamlit":
                print("\n🚀 Launching beautiful Streamlit UI...")
                print("💡 This will open in your browser with the new PRIDE-themed design!")
                input("Press Enter to continue...")
                subprocess.Popen(["python3", "-c", """
import subprocess
import sys
import os
os.chdir('/Users/piyushtiwari/For_Projects/Offtoken')
subprocess.run(['source', '.venv/bin/activate', '&&', 'streamlit', 'run', 'app.py'], shell=True)
                """])
            elif selected == "pages":
                print("\n🌍 Opening GitHub Pages preview...")
                subprocess.Popen(["python3", "preview_pages.py", "8081"])
                time.sleep(2)
                webbrowser.open("http://localhost:8081")
            elif selected == "security":
                print("\n🔒 Running security tests...")
                run_command("python3 test_security.py", "Security Test Suite")
            elif selected == "tests":
                print("\n🧪 Running core tests...")
                run_command("python3 test.py", "Core Test Suite")
            elif selected == "docker":
                print("\n🐳 Building Docker image...")
                run_command("docker build -t tokenforge .", "Docker Build")
            elif selected == "docs":
                print("\n📖 Available documentation:")
                docs = [
                    "README.md - Main project documentation",
                    "DEPLOYMENT.md - Complete deployment guide", 
                    "SECURITY.md - Security policy and guidelines",
                    "SECURITY_CHECKLIST.md - Security procedures"
                ]
                for doc in docs:
                    print(f"   📄 {doc}")
        
        except KeyboardInterrupt:
            print("\n\n👋 Demo interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

def main():
    """Main demo function"""
    print_banner()
    
    print("\n🎉 Welcome to the TokenForge Feature Demo!")
    print("This script showcases all the amazing new features and capabilities.")
    
    # Check if we're in the right directory
    if not Path("app.py").exists():
        print("\n❌ Error: Please run this script from the TokenForge project root directory")
        sys.exit(1)
    
    try:
        # Show features
        demo_features()
        
        # Show deployment options
        show_deployment_options()
        
        # Interactive demo
        print("\n" + "=" * 60)
        response = input("🎮 Would you like to try the interactive demo? (y/n): ").lower().strip()
        
        if response in ['y', 'yes']:
            interactive_demo()
        else:
            print("\n🚀 Great! Here's how to get started:")
            print("   🏠 Local: python3 setup.py")
            print("   🌍 Pages: python3 preview_pages.py")
            print("   🐳 Docker: docker-compose up -d")
            print("\n✨ Enjoy your beautiful TokenForge experience!")
    
    except KeyboardInterrupt:
        print("\n\n👋 Demo stopped by user. Thanks for exploring TokenForge!")
    except Exception as e:
        print(f"\n❌ Demo error: {e}")
        print("💡 Please check your installation and try again.")

if __name__ == "__main__":
    main()
