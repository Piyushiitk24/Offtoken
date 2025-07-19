#!/usr/bin/env python3
"""
Test Security Measures
Tests that the security scanner properly detects secrets
"""

import tempfile
import os
from pathlib import Path
import sys

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from security_scan import SecurityScanner

def test_secret_detection():
    """Test that the security scanner detects various types of secrets"""
    print("🧪 Testing security scanner...")
    
    # Create temporary test files with secrets
    test_cases = [
        {
            'filename': 'test_api_key.py',
            'content': 'API_KEY = "sk-1234567890abcdef1234567890abcdef12345678"',
            'should_detect': True,
            'description': 'OpenAI API key'
        },
        {
            'filename': 'test_safe.py',
            'content': 'API_KEY = "your-api-key-here"',
            'should_detect': False,
            'description': 'Whitelisted placeholder'
        },
        {
            'filename': 'test_password.py',
            'content': 'PASSWORD = "super_secret_password_123"',
            'should_detect': True,
            'description': 'Password'
        },
        {
            'filename': 'test_normal.py',
            'content': 'print("Hello, world!")',
            'should_detect': False,
            'description': 'Normal code'
        }
    ]
    
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        # Create test files
        for test_case in test_cases:
            file_path = temp_path / test_case['filename']
            with open(file_path, 'w') as f:
                f.write(test_case['content'])
        
        # Run scanner
        scanner = SecurityScanner(str(temp_path))
        findings = scanner.scan_project()
        
        # Check results
        results = []
        for test_case in test_cases:
            file_findings = [f for f in findings if test_case['filename'] in f['file']]
            detected = len(file_findings) > 0
            
            if detected == test_case['should_detect']:
                status = "✅ PASS"
            else:
                status = "❌ FAIL"
            
            results.append({
                'test': test_case['description'],
                'expected': 'DETECT' if test_case['should_detect'] else 'IGNORE',
                'actual': 'DETECTED' if detected else 'IGNORED',
                'status': status
            })
            
            print(f"  {status} {test_case['description']}: "
                  f"Expected {test_case['should_detect']}, Got {detected}")
    
    # Summary
    passed = sum(1 for r in results if 'PASS' in r['status'])
    total = len(results)
    
    print(f"\n📊 Test Results: {passed}/{total} passed")
    
    if passed == total:
        print("✅ All security tests passed!")
        return True
    else:
        print("❌ Some security tests failed!")
        return False

def test_gitignore_patterns():
    """Test that .gitignore properly excludes sensitive files"""
    print("\n🔍 Testing .gitignore patterns...")
    
    # Read .gitignore
    gitignore_path = Path(".gitignore")
    if not gitignore_path.exists():
        print("❌ .gitignore file not found!")
        return False
    
    with open(gitignore_path, 'r') as f:
        gitignore_content = f.read()
    
    # Check for essential patterns
    essential_patterns = [
        '.env',
        '*.key',
        'secrets.json',
        'config.ini',
        '__pycache__',
        '.venv',
        '*.log'
    ]
    
    missing_patterns = []
    for pattern in essential_patterns:
        if pattern not in gitignore_content:
            missing_patterns.append(pattern)
    
    if missing_patterns:
        print(f"❌ Missing patterns in .gitignore: {missing_patterns}")
        return False
    else:
        print("✅ All essential patterns found in .gitignore")
        return True

def main():
    """Run all security tests"""
    print("🔒 Security Test Suite")
    print("=" * 30)
    
    all_passed = True
    
    # Test secret detection
    if not test_secret_detection():
        all_passed = False
    
    # Test gitignore patterns
    if not test_gitignore_patterns():
        all_passed = False
    
    print("\n" + "=" * 30)
    if all_passed:
        print("🎉 All security tests passed!")
        print("🛡️  Your repository is properly secured!")
        return 0
    else:
        print("⚠️  Some security tests failed!")
        print("🔧 Please review and fix the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
