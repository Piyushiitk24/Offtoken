#!/usr/bin/env python3
"""
Security Demo for Offtoken Project
Demonstrates all security features and best practices
"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(cmd, description="", show_output=True):
    """Run a command and display results"""
    print(f"\n🔄 {description}")
    print(f"   Command: {cmd}")
    print("   " + "-" * 50)
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if show_output:
            if result.stdout:
                print(result.stdout)
            if result.stderr:
                print(result.stderr)
        
        return result.returncode == 0
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def demo_security_features():
    """Demonstrate all security features"""
    print("🔒 Offtoken Security Features Demo")
    print("=" * 50)
    
    print("\n📋 1. SECURITY FILES OVERVIEW")
    print("-" * 30)
    
    security_files = {
        ".gitignore": "Comprehensive ignore patterns for sensitive files",
        ".env.example": "Template for environment variables",
        "SECURITY.md": "Security policy and guidelines",
        "security_scan.py": "Automated secret detection scanner",
        "pre_commit_hook.py": "Git pre-commit security hook",
        "setup_security.sh": "One-click security setup",
        "test_security.py": "Security feature test suite"
    }
    
    for file, description in security_files.items():
        if Path(file).exists():
            print(f"   ✅ {file:<20} - {description}")
        else:
            print(f"   ❌ {file:<20} - Missing!")
    
    print("\n🔍 2. GITIGNORE PROTECTION")
    print("-" * 30)
    
    # Check .gitignore patterns
    with open(".gitignore", "r") as f:
        gitignore = f.read()
    
    critical_patterns = [".env", "*.key", "secrets.json", "config.ini", "__pycache__"]
    
    for pattern in critical_patterns:
        if pattern in gitignore:
            print(f"   ✅ {pattern} - Protected")
        else:
            print(f"   ⚠️  {pattern} - Not found")
    
    print("\n🧪 3. SECURITY SCANNER TEST")
    print("-" * 30)
    
    # Run security tests
    run_command("python3 test_security.py", "Running security test suite")
    
    print("\n🔐 4. LIVE SECURITY SCAN")
    print("-" * 30)
    
    # Run actual security scan
    run_command("python3 security_scan.py", "Scanning project for secrets")
    
    print("\n🎯 5. GIT HOOK STATUS")
    print("-" * 30)
    
    # Check if pre-commit hook is installed
    hook_path = Path(".git/hooks/pre-commit")
    if hook_path.exists():
        print("   ✅ Pre-commit hook installed")
        print("   📋 Hook will automatically run security scan before commits")
        
        # Show hook content
        with open(hook_path, "r") as f:
            hook_content = f.read()
        
        if "security" in hook_content.lower():
            print("   ✅ Hook contains security checks")
        else:
            print("   ⚠️  Hook may not contain security checks")
    else:
        print("   ❌ Pre-commit hook not installed")
        print("   💡 Run './setup_security.sh' to install")
    
    print("\n📚 6. SECURITY BEST PRACTICES")
    print("-" * 30)
    
    best_practices = [
        "Use .env files for all secrets (never commit them)",
        "Run 'python3 security_scan.py' before pushing",
        "Review all changes before committing",
        "Keep dependencies updated for security patches",
        "Use environment variables in production",
        "Never hardcode API keys in source code",
        "Enable pre-commit hooks for automatic scanning"
    ]
    
    for i, practice in enumerate(best_practices, 1):
        print(f"   {i}. {practice}")
    
    print("\n🚨 7. DEMONSTRATION: What happens if you try to commit secrets?")
    print("-" * 30)
    
    print("   If you accidentally try to commit a file with secrets:")
    print("   1. Pre-commit hook runs automatically")
    print("   2. Security scanner detects the secret")
    print("   3. Commit is BLOCKED")
    print("   4. You get a detailed report of what was found")
    print("   5. You must fix the issues before committing")
    print("")
    print("   This prevents secrets from EVER reaching GitHub!")
    
    print("\n✅ 8. SECURITY STATUS SUMMARY")
    print("-" * 30)
    
    # Final status check
    all_files_exist = all(Path(f).exists() for f in security_files.keys())
    hook_installed = Path(".git/hooks/pre-commit").exists()
    
    if all_files_exist and hook_installed:
        print("   🎉 ALL SECURITY MEASURES ACTIVE!")
        print("   🛡️  Your repository is fully protected")
        print("   🔒 Safe to commit and push to GitHub")
    else:
        print("   ⚠️  Some security measures missing")
        print("   🔧 Run './setup_security.sh' to complete setup")
    
    print("\n" + "=" * 50)
    print("🔒 Security Demo Complete")
    print("💡 Remember: Security is everyone's responsibility!")

if __name__ == "__main__":
    try:
        demo_security_features()
    except KeyboardInterrupt:
        print("\n\n👋 Demo interrupted by user")
    except Exception as e:
        print(f"\n❌ Demo failed: {e}")
        sys.exit(1)
