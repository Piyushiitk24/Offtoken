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

## 🎨 Project Structure

```
Offtoken/
├── app.py              # Main Streamlit application
├── setup.py            # One-click setup script
├── requirements.txt    # Python dependencies
├── test.py             # Test suite
├── sample.txt          # Sample document for testing
├── README.md           # This file
├── .gitignore          # Git ignore rules
└── .venv/              # Virtual environment
```

## 🤝 Contributing

This is a focused, production-ready tool. For feature requests or bug reports, please ensure they align with the core mission of providing accurate, professional token counting.

## 📄 License

MIT License - feel free to use in your projects!

---

**Note**: This tool provides the exact same token counts as OpenAI's APIs. Perfect for cost estimation and context management in production LLM applications.
