#!/usr/bin/env python3
"""
Security Scanner for Offtoken Project
Scans for potential secrets, API keys, and sensitive information before commits
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple, Dict
import subprocess
import json

class SecurityScanner:
    """Comprehensive security scanner for detecting secrets and sensitive data"""
    
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root).resolve()
        self.secrets_found = []
        
        # High-entropy patterns that often indicate secrets
        self.secret_patterns = {
            'api_key': r'(?i)(api[_-]?key|apikey)[\s]*[:=][\s]*["\']?([a-zA-Z0-9_\-]{20,})["\']?',
            'openai_key': r'sk-[a-zA-Z0-9]{48}',
            'anthropic_key': r'ant-api[0-9]{2}-[a-zA-Z0-9_\-]{93}',
            'secret_key': r'(?i)(secret[_-]?key|secretkey)[\s]*[:=][\s]*["\']?([a-zA-Z0-9_\-]{20,})["\']?',
            'password': r'(?i)(password|passwd|pwd)[\s]*[:=][\s]*["\']?([^\s\'"]{8,})["\']?',
            'token': r'(?i)(token|bearer)[\s]*[:=][\s]*["\']?([a-zA-Z0-9_\-]{20,})["\']?',
            'private_key': r'-----BEGIN (RSA )?PRIVATE KEY-----',
            'aws_key': r'AKIA[0-9A-Z]{16}',
            'github_token': r'ghp_[a-zA-Z0-9]{36}',
            'jwt_token': r'eyJ[a-zA-Z0-9_\-]+\.eyJ[a-zA-Z0-9_\-]+\.[a-zA-Z0-9_\-]+',
            'high_entropy': r'[a-zA-Z0-9_\-]{32,}',  # 32+ char alphanumeric strings
        }
        
        # File patterns to always scan
        self.scan_extensions = {'.py', '.txt', '.md', '.json', '.yaml', '.yml', '.env', '.ini', '.cfg', '.conf'}
        
        # Files to never scan
        self.exclude_patterns = {
            '*.pyc', '__pycache__', '.git', '.venv', 'node_modules', 
            '.pytest_cache', '.coverage', '*.log', '.DS_Store',
            'test_security.py'  # Exclude test file with intentional test secrets
        }
        
        # Whitelist for known safe patterns
        self.whitelist_patterns = [
            r'example[_-]?key',
            r'sample[_-]?token',
            r'placeholder',
            r'your[_-]?api[_-]?key[_-]?here',
            r'sk-your-openai-api-key-here',
            r'test[_-]?key',
            r'dummy[_-]?secret',
        ]

    def is_file_excluded(self, filepath: Path) -> bool:
        """Check if file should be excluded from scanning"""
        file_str = str(filepath)
        
        # Check against exclude patterns
        for pattern in self.exclude_patterns:
            if pattern in file_str or filepath.name.startswith('.'):
                return True
        
        # Only scan specific file types
        if filepath.suffix not in self.scan_extensions and not filepath.suffix == '':
            return True
            
        return False

    def is_whitelisted(self, content: str) -> bool:
        """Check if content matches whitelist patterns (safe to ignore)"""
        content_lower = content.lower()
        for pattern in self.whitelist_patterns:
            if re.search(pattern, content_lower, re.IGNORECASE):
                return True
        return False

    def scan_file(self, filepath: Path) -> List[Dict]:
        """Scan a single file for secrets"""
        findings = []
        
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                lines = content.split('\n')
                
                for line_num, line in enumerate(lines, 1):
                    for pattern_name, pattern in self.secret_patterns.items():
                        matches = re.finditer(pattern, line, re.IGNORECASE)
                        
                        for match in matches:
                            matched_text = match.group(0)
                            
                            # Skip if whitelisted
                            if self.is_whitelisted(matched_text):
                                continue
                            
                            # Special handling for high entropy - only flag if very suspicious
                            if pattern_name == 'high_entropy':
                                if len(matched_text) < 40 or not self._is_high_entropy(matched_text):
                                    continue
                            
                            findings.append({
                                'file': str(filepath.relative_to(self.project_root)),
                                'line': line_num,
                                'pattern': pattern_name,
                                'content': matched_text,
                                'context': line.strip()
                            })
                            
        except Exception as e:
            print(f"⚠️  Warning: Could not scan {filepath}: {e}")
        
        return findings

    def _is_high_entropy(self, text: str) -> bool:
        """Check if text has high entropy (randomness) indicating a potential secret"""
        if len(text) < 20:
            return False
        
        # Calculate character diversity
        unique_chars = len(set(text))
        entropy_ratio = unique_chars / len(text)
        
        # High entropy strings are more likely to be secrets
        return entropy_ratio > 0.7 and unique_chars > 10

    def scan_project(self) -> List[Dict]:
        """Scan entire project for secrets"""
        print(f"🔍 Scanning project: {self.project_root}")
        
        all_findings = []
        scanned_files = 0
        
        for root, dirs, files in os.walk(self.project_root):
            # Skip excluded directories
            dirs[:] = [d for d in dirs if not any(exc in d for exc in self.exclude_patterns)]
            
            for file in files:
                filepath = Path(root) / file
                
                if self.is_file_excluded(filepath):
                    continue
                
                scanned_files += 1
                findings = self.scan_file(filepath)
                all_findings.extend(findings)
        
        print(f"📂 Scanned {scanned_files} files")
        return all_findings

    def check_git_status(self) -> Dict:
        """Check git status for staged files that might contain secrets"""
        try:
            # Get staged files
            result = subprocess.run(['git', 'diff', '--cached', '--name-only'], 
                                  capture_output=True, text=True, cwd=self.project_root)
            staged_files = result.stdout.strip().split('\n') if result.stdout.strip() else []
            
            # Get untracked files
            result = subprocess.run(['git', 'ls-files', '--others', '--exclude-standard'], 
                                  capture_output=True, text=True, cwd=self.project_root)
            untracked_files = result.stdout.strip().split('\n') if result.stdout.strip() else []
            
            return {
                'staged': staged_files,
                'untracked': untracked_files
            }
        except Exception as e:
            print(f"⚠️  Warning: Could not check git status: {e}")
            return {'staged': [], 'untracked': []}

    def generate_report(self, findings: List[Dict]) -> str:
        """Generate a detailed security report"""
        report = []
        report.append("🔒 SECURITY SCAN REPORT")
        report.append("=" * 50)
        
        if not findings:
            report.append("✅ No potential secrets detected!")
            report.append("")
            report.append("Your repository appears secure for commit.")
        else:
            report.append(f"⚠️  Found {len(findings)} potential security issues:")
            report.append("")
            
            # Group by file
            by_file = {}
            for finding in findings:
                file = finding['file']
                if file not in by_file:
                    by_file[file] = []
                by_file[file].append(finding)
            
            for file, file_findings in by_file.items():
                report.append(f"📄 {file}")
                report.append("-" * len(file))
                
                for finding in file_findings:
                    report.append(f"  Line {finding['line']:3}: {finding['pattern']}")
                    report.append(f"       Content: {finding['content']}")
                    report.append(f"       Context: {finding['context'][:80]}...")
                    report.append("")
                
                report.append("")
        
        # Add recommendations
        report.append("🛡️  SECURITY RECOMMENDATIONS")
        report.append("-" * 30)
        report.append("1. Review all flagged content above")
        report.append("2. Move secrets to .env files (ignored by git)")
        report.append("3. Use environment variables for sensitive data")
        report.append("4. Never commit API keys or passwords")
        report.append("5. Run this scanner before each commit")
        report.append("")
        
        return "\n".join(report)

def main():
    """Main security scanner entry point"""
    scanner = SecurityScanner()
    
    print("🔒 Offtoken Security Scanner")
    print("=" * 40)
    
    # Scan for secrets
    findings = scanner.scan_project()
    
    # Check git status
    git_status = scanner.check_git_status()
    
    # Generate and display report
    report = scanner.generate_report(findings)
    print(report)
    
    # Special warnings for git operations
    if git_status['staged'] or git_status['untracked']:
        print("📋 GIT STATUS WARNING")
        print("-" * 20)
        
        if git_status['staged']:
            print("📤 Staged files (ready to commit):")
            for file in git_status['staged']:
                print(f"   • {file}")
        
        if git_status['untracked']:
            print("❓ Untracked files:")
            for file in git_status['untracked']:
                print(f"   • {file}")
        
        print("\n⚠️  Please verify these files don't contain secrets before committing!")
    
    # Exit with error code if secrets found
    if findings:
        print("\n❌ SCAN FAILED: Potential secrets detected!")
        print("   Please review and fix issues before committing.")
        sys.exit(1)
    else:
        print("\n✅ SCAN PASSED: Repository is secure for commit!")
        sys.exit(0)

if __name__ == "__main__":
    main()
