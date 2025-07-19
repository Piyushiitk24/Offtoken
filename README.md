# 🔢 Token Counter Pro

A **professional-grade token counting tool** with authentic tokenizers from OpenAI and other providers. Built for developers, researchers, and anyone who needs accurate token counting for LLM applications.

## ✨ Features

- **Real Tokenizers**: Uses `tiktoken` from OpenAI - the same tokenizers used by GPT-4, GPT-3.5, and other OpenAI models
- **Multiple Models**: GPT-4, GPT-3.5 Turbo, GPT-3, and various encodings (cl100k_base, p50k_base)
- **Document Support**: PDF, DOCX, TXT with OCR support for scanned documents
- **Cost Estimation**: Accurate API cost calculation with preset pricing for popular models
- **Professional UI**: Clean, modern Streamlit interface with detailed token analytics
- **Export Options**: CSV and TXT export with comprehensive usage data
- **Local Processing**: All tokenization happens locally - no API calls required

## 🚀 Quick Start

```bash
# One-command setup and launch
python3 setup.py
```

That's it! The script will:
1. Check system dependencies (Homebrew, Tesseract, Poppler)
2. Create a virtual environment
3. Install all dependencies
4. Launch the application at `http://localhost:8503`

## 🛠️ Manual Setup

```bash
# Install system dependencies (macOS)
brew install tesseract poppler

# Setup Python environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Launch application
streamlit run app.py
```

## 📊 Supported Tokenizers

All tokenizers use the **exact same algorithms** as their respective APIs:

- **GPT-4**: OpenAI GPT-4 (most accurate for GPT-4 API usage)
- **GPT-3.5 Turbo**: OpenAI GPT-3.5 Turbo (ChatGPT)
- **GPT-3**: OpenAI GPT-3 (text-davinci-003)
- **cl100k_base**: OpenAI encoding for GPT-4 and GPT-3.5
- **p50k_base**: OpenAI encoding for GPT-3 and Codex

## 🎯 Use Cases

- **API Cost Estimation**: Calculate exact costs before making API calls
- **Context Window Management**: Ensure text fits within model limits
- **Content Optimization**: Optimize prompts for efficiency
- **Research**: Analyze tokenization patterns across different models
- **Development**: Test and debug LLM applications

## 📱 How to Use

1. **Launch**: Run `python3 setup.py` or `streamlit run app.py`
2. **Select Model**: Choose your target tokenizer from the dropdown
3. **Input Text**: Upload a document or paste text directly
4. **Configure Costs**: Set pricing for cost estimation (optional)
5. **Analyze**: Get detailed token counts and analytics
6. **Export**: Download results as CSV or TXT

## 🔧 Technical Details

- **Framework**: Streamlit for the web interface
- **Tokenizers**: `tiktoken` library (official OpenAI tokenizers)
- **Document Processing**: `pdfplumber`, `python-docx`, `pytesseract`
- **OCR**: Tesseract for scanned document processing
- **Export**: Pandas for data export functionality

## 📋 Requirements

- **OS**: macOS (Intel/Apple Silicon)
- **Python**: 3.8+ (tested with 3.13)
- **System**: Homebrew for dependency management
- **Memory**: ~100MB for base installation

## 🧪 Testing

Run the test suite to verify functionality:

```bash
source .venv/bin/activate
python test.py
```

## 🔒 Privacy & Security

- **100% Local**: All processing happens on your device
- **No API Calls**: No internet required after initial setup
- **No Data Collection**: No usage tracking or data transmission
- **Secure**: Temporary files are automatically cleaned up
- **Secret Protection**: Pre-commit hooks prevent accidental secret uploads
- **Environment Variables**: Secure configuration with `.env` files
- **Security Scanning**: Built-in scanner detects potential secrets

## 🎨 Project Structure

```
Offtoken/
├── app.py              # Main Streamlit application
├── setup.py            # One-click setup script
├── requirements.txt    # Python dependencies
├── test.py             # Test suite
├── sample.txt          # Sample document for testing
├── README.md           # This file
├── SECURITY.md         # Security policy and guidelines
├── .gitignore          # Git ignore rules (includes security patterns)
├── .env.example        # Environment variables template
├── security_scan.py    # Security scanner for detecting secrets
├── pre_commit_hook.py  # Git pre-commit security hook
├── setup_security.sh   # Security setup script
├── .streamlit/         # Streamlit configuration
└── .venv/              # Virtual environment
```

## 🛡️ Security Features

### Automatic Protection
- **Pre-commit hooks**: Automatically scan for secrets before each commit
- **Comprehensive .gitignore**: Blocks sensitive files from being tracked
- **Environment templates**: Safe configuration with `.env.example`
- **High-entropy detection**: Identifies potential API keys and secrets

### Manual Security Tools
```bash
# Run security scan manually
python3 security_scan.py

# Set up security measures (one-time)
./setup_security.sh

# Check for potential secrets in files
python3 security_scan.py --verbose
```

### Best Practices
1. **Never commit secrets**: Use environment variables instead
2. **Use .env files**: Copy `.env.example` to `.env` and add your secrets
3. **Run security scans**: Before pushing to GitHub
4. **Review changes**: Always check what you're committing
5. **Keep dependencies updated**: Regular security updates

## 🤝 Contributing

This is a focused, production-ready tool. For feature requests or bug reports, please ensure they align with the core mission of providing accurate, professional token counting.

## 📄 License

MIT License - feel free to use in your projects!

---

**Note**: This tool provides the exact same token counts as OpenAI's APIs. Perfect for cost estimation and context management in production LLM applications.
