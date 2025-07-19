#!/usr/bin/env python3
"""
Git Pre-commit Hook for Security
Automatically runs security scan before each commit
"""

import sys
import subprocess
import os
from pathlib import Path

def run_security_scan():
    """Run the security scanner"""
    script_dir = Path(__file__).parent
    security_script = script_dir / "security_scan.py"
    
    print("🔒 Running pre-commit security scan...")
    
    try:
        result = subprocess.run([sys.executable, str(security_script)], 
                              capture_output=True, text=True)
        
        # Print the output
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        
        # Return the exit code
        return result.returncode
        
    except Exception as e:
        print(f"❌ Error running security scan: {e}")
        return 1

def main():
    """Main pre-commit hook"""
    print("🚨 Git Pre-commit Security Check")
    print("=" * 35)
    
    exit_code = run_security_scan()
    
    if exit_code != 0:
        print("\n🛑 COMMIT BLOCKED!")
        print("   Security scan failed. Please fix issues before committing.")
        print("   Run 'python security_scan.py' to see details.")
        sys.exit(1)
    else:
        print("\n✅ Security check passed. Proceeding with commit...")
        sys.exit(0)

if __name__ == "__main__":
    main()
