# ✨ TokenForge - Professional AI Token Counter & Cost Calculator

> **Beautiful PRIDE-themed token analysis tool with authentic OpenAI tokenizers**

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Demo-brightgreen?style=for-the-badge&logo=github)](https://piyushiitk24.github.io/Offtoken/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue?style=for-the-badge&logo=docker)](https://hub.docker.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-Cloud%20Ready-red?style=for-the-badge&logo=streamlit)](https://streamlit.io/cloud)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Security](https://img.shields.io/badge/Security-A%2B-green?style=for-the-badge&logo=security)](SECURITY.md)

**TokenForge** is a professional-grade AI token counting and cost estimation tool featuring a stunning PRIDE-themed user interface. Built for developers, researchers, AI engineers, and content creators who need accurate token analysis for GPT-4, GPT-3.5, and other OpenAI language models.

## 🌟 **Why TokenForge?**

### 🎯 **100% Accurate Token Counting**
- Uses **authentic OpenAI tiktoken library** - the same tokenizers used by GPT-4 and ChatGPT
- **Exact same algorithms** as OpenAI APIs for guaranteed accuracy
- Supports GPT-4, GPT-3.5 Turbo, GPT-3, cl100k_base, and p50k_base encodings

### 🎨 **Beautiful PRIDE-Themed Interface**
- **Stunning visual design** with subtle PRIDE color palette celebrating diversity
- **Smooth animations** and modern card-based layout
- **Fully responsive** - perfect on desktop, tablet, and mobile
- **Professional aesthetics** suitable for enterprise environments

### 💰 **Smart Cost Estimation**
- **Real-time API cost calculation** with preset pricing for popular models
- **Budget planning tools** for large-scale AI projects
- **Token efficiency analysis** to optimize your prompts and content

### 🔒 **Privacy-First Architecture**
- **100% local processing** - your documents never leave your device
- **No API calls required** - works completely offline after setup
- **Enterprise-grade security** with automated secret detection
- **No data collection** or tracking whatsoever

## 🚀 **Quick Start Guide**

### ⚡ **One-Command Launch** (Recommended)
```bash
# Clone and launch in seconds
git clone https://github.com/Piyushiitk24/Offtoken.git
cd Offtoken
python3 setup.py
```

### 🔧 **Manual Setup** (Advanced Users)
```bash
# Prerequisites: Python 3.8+, Homebrew (macOS)
brew install tesseract poppler

# Environment setup
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Launch with beautiful UI
streamlit run app.py
```

### � **Interactive Demo**
```bash
# Experience all features
python3 demo_tokenforge.py

# Quick launcher with options
python3 start.py
```

## �🌐 **Multiple Deployment Options**

TokenForge supports deployment anywhere - from local development to enterprise cloud:

| Deployment Type | Command | Best For | Setup Time |
|-----------------|---------|----------|------------|
| 🏠 **Local** | `python3 setup.py` | Development, Privacy | 2 minutes |
| ☁️ **Streamlit Cloud** | Fork → Connect → Deploy | Team Sharing | 5 minutes |
| 🌍 **GitHub Pages** | Auto-deployed | Documentation | Automatic |
| 🐳 **Docker** | `docker-compose up -d` | Production | 3 minutes |

**📖 Complete deployment guide:** [DEPLOYMENT.md](DEPLOYMENT.md)

## 🎨 **Visual Showcase**

### 🌈 **PRIDE-Themed Design System**
- **Hero Sections**: Gradient backgrounds with smooth animations
- **Interactive Cards**: Professional hover effects and transitions  
- **Smart Metrics**: Color-coded analytics with PRIDE accent colors
- **Responsive Layout**: Perfect experience on any screen size

### 📊 **Professional Analytics**
- **Token Efficiency Ratios**: Optimize your content for specific models
- **Cost Breakdown Analysis**: Detailed pricing estimates with export
- **First Token Previews**: See exactly how your text gets tokenized
- **Comprehensive Reports**: Professional CSV and TXT exports

## 📊 **Supported AI Models & Tokenizers**

TokenForge uses **authentic OpenAI tokenizers** for 100% accurate results:

| Model | Tokenizer | Description | Best For |
|-------|-----------|-------------|----------|
| **GPT-4** | `gpt-4` | Latest OpenAI model | Most accurate GPT-4 API usage |
| **GPT-3.5 Turbo** | `gpt-3.5-turbo` | ChatGPT model | ChatGPT and GPT-3.5 APIs |
| **GPT-3** | `text-davinci-003` | Legacy GPT-3 | text-davinci-003 API |
| **cl100k_base** | `cl100k_base` | Modern encoding | GPT-4, GPT-3.5 compatible |
| **p50k_base** | `p50k_base` | Classic encoding | GPT-3, Codex compatible |

## 🎯 **Use Cases & Applications**

### 💰 **API Cost Optimization**
- **Pre-flight cost estimation** before expensive API calls
- **Budget planning** for large-scale AI projects  
- **Prompt optimization** to reduce token usage
- **ROI analysis** for AI content generation

### 📏 **Context Window Management**
- **Ensure prompts fit** within model limits (8K/32K tokens)
- **Optimize content length** for specific models
- **Avoid costly API failures** due to token limits
- **Smart content chunking** for large documents

### 🔬 **AI Research & Development**
- **Compare tokenization** across different models
- **Analyze text compression** ratios and efficiency
- **Academic research** on language model behavior
- **Content optimization** studies and analysis

### 🎨 **Content Creation & Marketing**
- **Optimize marketing copy** for token efficiency
- **Streamline documentation** and technical content
- **Perfect prompt engineering** for specific token counts
- **Content audit** and optimization workflows

## 📱 **How to Use TokenForge**

### 🚀 **Step-by-Step Guide**
1. **Launch Application**: Use any deployment method above
2. **Select AI Model**: Choose your target tokenizer (GPT-4, GPT-3.5, etc.)
3. **Input Content**: Upload documents (PDF/DOCX/TXT) or paste text
4. **Configure Pricing**: Set API costs for accurate estimation (optional)
5. **Analyze Results**: Get detailed token counts with beautiful visualizations
6. **Export Reports**: Download professional CSV or TXT reports

### 💡 **Pro Tips for Best Results**
- **Use model-specific tokenizers** for most accurate API cost estimation
- **Test different models** to find the most efficient tokenization
- **Export results** for record-keeping and budget planning
- **Leverage OCR features** for scanned documents and images

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
