# ✨ TokenForge - Professional Token Counter

A **beautiful, professional-grade token counting tool** with authentic tokenizers and stunning PRIDE-themed UI. Built for developers, researchers, and AI enthusiasts who demand accuracy and style.

## 🎨 Beautiful New UI

**TokenForge** now features a completely redesigned interface with:
- ✨ **Stunning PRIDE-themed colors** - Subtle, professional, and inclusive design
- 🎯 **Modern card-based layout** - Clean, organized, and intuitive
- 📱 **Fully responsive design** - Perfect on desktop, tablet, and mobile
- 🌈 **Smooth animations** - Delightful interactions and transitions
- 🎭 **Dark mode support** - Adapts to your system preferences

## ✨ Features

- **🎯 Authentic Tokenizers**: Uses `tiktoken` from OpenAI - the same tokenizers used by GPT-4, GPT-3.5, and other OpenAI models
- **📄 Multi-Format Support**: PDF, DOCX, TXT with OCR support for scanned documents
- **💰 Smart Cost Estimation**: Accurate API cost calculation with preset pricing for popular models
- **🎨 Beautiful Interface**: Modern, PRIDE-themed UI with smooth animations and responsive design
- **📊 Detailed Analytics**: Comprehensive token analysis with breakdowns and efficiency metrics
- **📥 Export Options**: CSV and TXT export with detailed usage data
- **🔒 Privacy First**: 100% local processing - no API calls or data collection required

## 🚀 Quick Start

### One-Command Launch (Recommended)
```bash
# Clone and launch in one go
git clone https://github.com/Piyushiitk24/Offtoken.git
cd Offtoken
python3 setup.py
```

### Manual Setup
```bash
# Install system dependencies (macOS)
brew install tesseract poppler

# Setup Python environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Launch with beautiful UI
streamlit run app.py
```

## 🌐 Deployment Options

TokenForge supports multiple deployment methods:

### 🏠 Local Development
Perfect for private use and development:
```bash
python3 setup.py  # One-command setup
```

### ☁️ Streamlit Cloud
Easy sharing and collaboration:
1. Fork this repository
2. Connect to [Streamlit Cloud](https://streamlit.io/cloud)
3. Deploy with one click!

### 🌍 GitHub Pages
Static landing page with deployment instructions:
- Automatically deploys to `https://yourusername.github.io/Offtoken`
- Beautiful responsive design
- Direct links to local setup

### 🐳 Docker
Production-ready containerized deployment:
```bash
# Quick start with Docker
docker-compose up -d

# Or build manually
docker build -t tokenforge .
docker run -p 8501:8501 tokenforge
```

**📖 See [DEPLOYMENT.md](DEPLOYMENT.md) for complete deployment guide**

## 🎨 UI Screenshots

### 🌈 Beautiful PRIDE-Themed Interface
- **Hero Section**: Stunning gradient backgrounds with smooth animations
- **Interactive Cards**: Hover effects and professional styling
- **Smart Metrics**: Color-coded analytics with PRIDE accent colors
- **Responsive Design**: Perfect on all screen sizes

### 📊 Enhanced Analytics
- **Token Efficiency**: Real-time token-to-word ratios
- **Cost Breakdown**: Detailed pricing analysis
- **Export Ready**: Professional reports in multiple formats

## 📊 Supported Tokenizers

All tokenizers use the **exact same algorithms** as their respective APIs:

| Model | Description | Use Case |
|-------|-------------|----------|
| **GPT-4** | OpenAI GPT-4 | Most accurate for GPT-4 API usage |
| **GPT-3.5 Turbo** | OpenAI GPT-3.5 | ChatGPT and GPT-3.5 APIs |
| **GPT-3** | OpenAI GPT-3 | Legacy text-davinci-003 |
| **cl100k_base** | OpenAI encoding | GPT-4 and GPT-3.5 compatible |
| **p50k_base** | OpenAI encoding | GPT-3 and Codex compatible |

## 🎯 Use Cases

### 💰 **API Cost Planning**
- Calculate exact costs before making expensive API calls
- Optimize prompts for maximum efficiency
- Budget planning for large-scale projects

### 📏 **Context Window Management**
- Ensure text fits within model limits (8K/32K tokens)
- Perfect for GPT-4's context constraints
- Avoid costly API failures

### 🔬 **Research & Development**
- Analyze tokenization patterns across models
- Compare efficiency between different approaches
- Academic research and optimization studies

### 🎨 **Content Optimization**
- Optimize marketing copy for token efficiency
- Streamline documentation and content
- Perfect prompts for specific token counts

## 📱 How to Use TokenForge

1. **🚀 Launch**: Run `python3 setup.py` or use any deployment method
2. **🤖 Select Model**: Choose your target tokenizer from the beautiful dropdown
3. **📄 Input Content**: Upload documents or paste text directly
4. **💰 Set Pricing**: Configure cost estimation (optional)
5. **📊 Analyze**: Get detailed token counts and beautiful analytics
6. **📥 Export**: Download professional reports as CSV or TXT

## 🔧 Technical Architecture

### 🎨 **Frontend**
- **Framework**: Streamlit with custom CSS
- **Design System**: PRIDE-themed color palette
- **Responsive**: Mobile-first design approach
- **Animations**: Smooth CSS transitions and effects

### 🧠 **Backend** 
- **Tokenizers**: Official `tiktoken` library (OpenAI)
- **Document Processing**: `pdfplumber`, `python-docx`, `pytesseract`
- **OCR Engine**: Tesseract for scanned documents
- **Export Engine**: Pandas for data manipulation

### 🏗️ **Architecture**
- **100% Local**: No external API dependencies
- **Secure**: All processing happens on your device
- **Fast**: Optimized for performance and responsiveness
- **Scalable**: Docker-ready for production deployment

## 📋 System Requirements

### **Minimum Requirements**
- **OS**: macOS (Intel/Apple Silicon), Linux, Windows
- **Python**: 3.8+ (tested with 3.11-3.13)
- **Memory**: 512MB RAM
- **Storage**: 500MB for dependencies

### **Recommended Specifications**
- **OS**: macOS with Homebrew
- **Python**: 3.11+
- **Memory**: 1GB+ RAM
- **Storage**: 1GB+ available space
- **Network**: Only for initial setup

### **System Dependencies**
- **Tesseract**: OCR processing
- **Poppler**: PDF rendering
- **Homebrew**: Package management (macOS)

## 🧪 Testing & Quality

### **Automated Testing**
```bash
# Run comprehensive test suite
python test.py

# Run security tests
python test_security.py

# Test all features
python demo_security.py
```

### **Security Testing**
- ✅ **Secret Detection**: Prevents API key leaks
- ✅ **Pre-commit Hooks**: Automatic security scanning
- ✅ **Privacy Audit**: No data transmission verification
- ✅ **Dependency Scanning**: Regular security updates

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
TokenForge/
├── 🎨 Frontend & UI
│   ├── app.py                      # Main Streamlit app with PRIDE-themed UI
│   ├── .streamlit/                 # Streamlit configuration
│   │   ├── config.toml            # Production config
│   │   └── config.toml.example    # Template config
│   └── docs/                      # GitHub Pages site
│       └── index.html             # Beautiful landing page
│
├── 🚀 Deployment & DevOps
│   ├── Dockerfile                 # Production container
│   ├── docker-compose.yml         # Easy deployment
│   ├── .github/workflows/         # CI/CD pipelines
│   │   └── deploy.yml            # Auto-deploy to GitHub Pages
│   ├── DEPLOYMENT.md              # Complete deployment guide
│   └── setup.py                   # One-click local setup
│
├── 🔒 Security & Privacy
│   ├── .gitignore                 # Comprehensive security patterns
│   ├── .env.example               # Environment template
│   ├── SECURITY.md                # Security policy
│   ├── SECURITY_CHECKLIST.md      # Security procedures
│   ├── security_scan.py           # Automated secret detection
│   ├── pre_commit_hook.py         # Git security hooks
│   ├── setup_security.sh          # Security setup script
│   └── test_security.py           # Security test suite
│
├── 🧪 Testing & Quality
│   ├── test.py                    # Core functionality tests
│   ├── test_security.py           # Security validation
│   └── demo_security.py           # Security demonstration
│
├── 📊 Core Engine
│   ├── requirements.txt           # Python dependencies
│   └── sample.txt                 # Test document
│
└── 📚 Documentation
    ├── README.md                  # This comprehensive guide
    ├── DEPLOYMENT.md              # Deployment instructions
    ├── SECURITY.md                # Security guidelines
    └── SECURITY_CHECKLIST.md      # Security procedures
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

## 🤝 Contributing

TokenForge is built with love for the developer community! Here's how you can contribute:

### 🎨 **UI/UX Improvements**
- Enhance the PRIDE-themed design system
- Add new animations and interactions
- Improve responsive design patterns
- Suggest accessibility improvements

### 🔧 **Feature Development**
- Add support for new tokenizers
- Implement additional export formats
- Create new analysis visualizations
- Enhance document processing capabilities

### 🧪 **Testing & Quality**
- Write comprehensive tests
- Improve security measures
- Add performance optimizations
- Document edge cases and solutions

### 📖 **Documentation**
- Improve setup instructions
- Add deployment examples
- Create video tutorials
- Write technical deep-dives

### 🚀 **Deployment & DevOps**
- Optimize Docker configurations
- Add new cloud platform support
- Improve CI/CD pipelines
- Create monitoring solutions

**Please ensure all contributions:**
- ✅ Follow the security guidelines in `SECURITY.md`
- ✅ Include appropriate tests
- ✅ Maintain the PRIDE-themed design language
- ✅ Are compatible with all deployment methods

## 📄 License

**MIT License** - Feel free to use TokenForge in your projects!

This project is open source and welcomes contributions from developers worldwide. The PRIDE-themed design celebrates diversity and inclusion in the tech community.

## 🌟 Acknowledgments

### **Special Thanks**
- 🏳️‍🌈 **PRIDE Community** - For inspiring inclusive design
- 🤖 **OpenAI Team** - For the excellent tiktoken library
- 🚀 **Streamlit Team** - For the amazing framework
- 💖 **Contributors** - Everyone who makes this project better

### **Powered By**
- **[tiktoken](https://github.com/openai/tiktoken)** - Official OpenAI tokenizers
- **[Streamlit](https://streamlit.io/)** - Beautiful web framework
- **[Tesseract](https://github.com/tesseract-ocr/tesseract)** - OCR engine
- **[pdfplumber](https://github.com/jsvine/pdfplumber)** - PDF processing

---

<div align="center">

**✨ TokenForge - Where Precision Meets Beauty ✨**

*Professional token analysis with a touch of PRIDE*

**Made with 💖 for developers, researchers, and AI enthusiasts everywhere**

[🚀 Get Started](DEPLOYMENT.md) • [🔒 Security](SECURITY.md) • [🐛 Issues](https://github.com/Piyushiitk24/Offtoken/issues) • [⭐ Star us on GitHub](https://github.com/Piyushiitk24/Offtoken)

</div>
