#!/usr/bin/env python3
"""
Preview GitHub Pages Site Locally
Opens the static landing page in your browser
"""

import webbrowser
import http.server
import socketserver
import os
import sys
from pathlib import Path
import threading
import time

def serve_static_site(port=8080):
    """Serve the static GitHub Pages site locally"""
    docs_dir = Path(__file__).parent / "docs"
    
    if not docs_dir.exists():
        print("❌ docs/ directory not found!")
        print("💡 Make sure you're running this from the project root")
        return False
    
    # Change to docs directory
    os.chdir(docs_dir)
    
    # Create server
    handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            print(f"🌐 Serving GitHub Pages site at http://localhost:{port}")
            print("📄 Serving from: docs/index.html")
            print("🚀 Opening in browser...")
            print("⏹️  Press Ctrl+C to stop")
            
            # Open browser after a short delay
            def open_browser():
                time.sleep(1)
                webbrowser.open(f"http://localhost:{port}")
            
            browser_thread = threading.Thread(target=open_browser)
            browser_thread.daemon = True
            browser_thread.start()
            
            # Serve the site
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
        return True
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Port {port} is already in use!")
            print(f"💡 Try a different port: python preview_pages.py {port + 1}")
        else:
            print(f"❌ Error starting server: {e}")
        return False

def main():
    """Main function"""
    print("🎨 TokenForge GitHub Pages Preview")
    print("=" * 40)
    
    # Get port from command line or use default
    port = 8080
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("❌ Invalid port number")
            sys.exit(1)
    
    # Check if we're in the right directory
    if not Path("docs/index.html").exists():
        print("❌ docs/index.html not found!")
        print("💡 Make sure you're running this from the TokenForge project root")
        sys.exit(1)
    
    # Serve the site
    success = serve_static_site(port)
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
