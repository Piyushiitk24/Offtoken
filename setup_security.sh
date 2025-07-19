#!/bin/bash

# ==============================================================================
# Security Setup Script for Offtoken Project
# Configures git hooks and security measures
# ==============================================================================

set -e  # Exit on any error

echo "🔒 Setting up security measures for Offtoken..."
echo "================================================"

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_ROOT"

# Create .git/hooks directory if it doesn't exist
mkdir -p .git/hooks

# Install pre-commit hook
echo "📋 Installing git pre-commit hook..."
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
# Auto-generated security pre-commit hook
# Runs security scan before each commit

python3 "$(dirname "$0")/../../pre_commit_hook.py"
EOF

# Make the hook executable
chmod +x .git/hooks/pre-commit

# Test the security scanner
echo "🧪 Testing security scanner..."
python3 security_scan.py

echo ""
echo "✅ Security setup complete!"
echo ""
echo "🛡️  Security measures now active:"
echo "   • .gitignore configured to block sensitive files"
echo "   • Pre-commit hook will scan for secrets"
echo "   • Environment template (.env.example) created"
echo "   • Security scanner available (python3 security_scan.py)"
echo ""
echo "📋 Best practices:"
echo "   • Always use .env files for secrets (never commit them)"
echo "   • Run 'python3 security_scan.py' before pushing"
echo "   • Review all changes before committing"
echo "   • Use environment variables in production"
echo ""
echo "🔒 Your repository is now secured against accidental secret uploads!"
