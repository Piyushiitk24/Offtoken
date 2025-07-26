# TokenForge - Professional AI Token Counter

<div align="center">

![TokenForge](https://img.shields.io/badge/TokenForge-AI%20Tool-rainbow)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red)
![License](https://img.shields.io/badge/License-MIT-green)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-brightgreen)](https://piyushiitk24.github.io/Offtoken/)

**🌈 Professional AI token counter with beautiful UI for OpenAI models**

**Two Ways to Use:**
- **🌐 [Web App](https://piyushiitk24.github.io/Offtoken/webapp.html)** - Instant access in your browser
- **🏠 [Local App](#local-setup)** - Maximum privacy & offline use

[🌐 **Try Online Now**](https://piyushiitk24.github.io/Offtoken/webapp.html) • [� **Local Setup**](#local-setup) • [📊 Features](#features) • [🎯 Use Cases](#use-cases)

</div>

---

## 🌐 Web App (Instant Access)

**Perfect for quick token analysis without any installation!**

✅ **Instant access** - No downloads or setup required  
✅ **Complete privacy** - All processing happens in your browser  
✅ **Full functionality** - Token counting, cost estimation, file uploads  
✅ **Mobile friendly** - Works on phones and tablets  

**[🚀 Launch Web App Now](https://piyushiitk24.github.io/Offtoken/webapp.html)**

---

## 🔒 Local Setup (Maximum Privacy)

**For sensitive documents, offline use, and maximum features:**

### ⚡ Quick Start
```bash
git clone https://github.com/Piyushiitk24/Offtoken.git
cd Offtoken
python3 setup.py
```

### 🛠️ Manual Setup
```bash
git clone https://github.com/Piyushiitk24/Offtoken.git
cd Offtoken
pip install -r requirements.txt
streamlit run app.py
```

### 🌟 Local App Benefits
✅ **Complete offline** - No internet required after setup  
✅ **OCR support** - Process scanned PDFs with text extraction  
✅ **Maximum privacy** - Documents never leave your device  
✅ **Advanced features** - Full Streamlit interface with more options  
✅ **Better performance** - Native Python processing  

---

## 📊 Features

### ✨ **Core Functionality**
- **Authentic Tokenizers** - Uses real OpenAI tiktoken library
- **Multi-Model Support** - GPT-4, GPT-3.5, GPT-3, Codex, and more
- **Document Processing** - PDF, DOCX, TXT file support
- **API Cost Estimation** - Accurate pricing for all major models
- **Professional Reports** - Export detailed analytics as CSV/TXT

### 🎨 **Beautiful Interface**
- **Modern Design** - Clean, professional UI with subtle PRIDE theming
- **Responsive Layout** - Works perfectly on all devices
- **Interactive Analytics** - Real-time visualizations and metrics
- **Intuitive UX** - Easy-to-use interface for all skill levels

### 🔒 **Privacy & Security**
- **Local Processing** - Your data never leaves your device
- **No Tracking** - Zero data collection or analytics
- **Secure** - Open source and transparent
- **Offline Ready** - Works without internet connection

## 📊 Supported Models

| Provider | Model | Web App | Local App | Tokenizer | Best For |
|----------|-------|---------|-----------|-----------|----------|
| **OpenAI** | GPT-4 / GPT-4 Turbo | ✅ | ✅ | cl100k_base | Most accurate GPT-4 API usage |
| **OpenAI** | GPT-3.5 Turbo | ✅ | ✅ | cl100k_base | ChatGPT and GPT-3.5 APIs |
| **OpenAI** | GPT-4o | ✅ | ✅ | cl100k_base | Latest multimodal model |
| **OpenAI** | GPT-3 (Davinci) | ✅ | ✅ | p50k_base | Legacy GPT-3 applications |
| **OpenAI** | Codex | ✅ | ✅ | p50k_base | GitHub Copilot and code models |
| **Anthropic** | Claude 3 Opus | ✅* | ✅ | cl100k_base* | Long context, complex reasoning |
| **Anthropic** | Claude 3 Sonnet | ✅* | ✅ | cl100k_base* | Balanced performance |
| **Anthropic** | Claude 3 Haiku | ✅* | ✅ | cl100k_base* | Fast, cost-effective |
| **Anthropic** | Claude 2 | ✅* | ✅ | cl100k_base* | Previous generation |
| **Google** | Gemini Pro | ✅* | ✅ | cl100k_base* | Google's flagship model |
| **Google** | Gemini Pro Vision | ✅* | ✅ | cl100k_base* | Multimodal capabilities |
| **Google** | Gemini Ultra | ✅* | ✅ | cl100k_base* | Most capable Google model |
| **xAI** | Grok-1 | ✅* | ✅ | cl100k_base* | Real-time information |
| **xAI** | Grok-1.5 | ✅* | ✅ | cl100k_base* | Enhanced capabilities |
| **Meta** | Llama 2 (70B/13B/7B) | ✅* | ✅ | cl100k_base* | Open source models |
| **Mistral** | Large/Medium/Small | ✅* | ✅ | cl100k_base* | European AI models |

**\* Note:** Non-OpenAI models use OpenAI tokenizer approximations in the web app. Local app may include native tokenizers for some models.

## 🎯 Use Cases

### 💰 **API Cost Optimization**
- Pre-flight cost estimation before expensive API calls
- Budget planning for large-scale AI projects
- Prompt optimization to reduce token usage

### 📏 **Context Window Management**
- Ensure prompts fit within model limits (8K/32K/128K tokens)
- Optimize content length for specific models
- Avoid costly API failures due to token limits

### 🔬 **Research & Development**
- Compare tokenization across different models
- Analyze text compression ratios and efficiency
- Academic research on language model behavior

### 📄 **Document Analysis**
- **Web App**: Process text-based PDFs and documents instantly
- **Local App**: OCR support for scanned documents and images

### 🎨 **Content Creation**
- Optimize marketing copy for token efficiency
- Streamline documentation and technical content
- Perfect prompt engineering for specific token counts

## � Which Version Should I Use?

### 🌐 **Use Web App When:**
- You need quick token counts
- Working with text or text-based documents
- Want instant access without installation
- On mobile or shared computers
- Doing general API cost estimation

### 🔒 **Use Local App When:**
- Processing sensitive or confidential documents
- Need OCR for scanned PDFs or images
- Want complete offline functionality
- Require advanced features and customization
- Working in environments with internet restrictions

## 📱 How to Use

### Web App:
1. **🌐 Visit**: Go to [webapp.html](https://piyushiitk24.github.io/Offtoken/webapp.html)
2. **🤖 Select Model**: Choose your target tokenizer
3. **📄 Input Content**: Upload documents or paste text
4. **💰 Set Pricing**: Configure cost estimation (optional)
5. **📊 Analyze**: View detailed token counts and analytics
6. **📥 Export**: Download professional reports

### Local App:
1. **🔧 Setup**: Run `python3 setup.py`
2. **🚀 Launch**: Streamlit opens automatically in your browser
3. **📄 Upload Files**: Including scanned PDFs with OCR
4. **🤖 Configure**: Choose models and settings
5. **📊 Analyze**: Get comprehensive token analysis
6. **📥 Export**: Download detailed reports

## 🛠️ Requirements

### Web App:
- **Modern Browser** (Chrome, Firefox, Safari, Edge)
- **JavaScript Enabled**
- **No installation required**

### Local App:
- **Python 3.8+** (tested with 3.11-3.13)
- **Operating System**: macOS, Linux, Windows
- **Memory**: 512MB RAM minimum
- **Dependencies**: Automatically installed by setup script

## 📖 Documentation

- **[GitHub Pages](https://piyushiitk24.github.io/Offtoken/)** - Full documentation and web app
- **[Issues](https://github.com/Piyushiitk24/Offtoken/issues)** - Bug reports and feature requests
- **[Discussions](https://github.com/Piyushiitk24/Offtoken/discussions)** - Community support

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

<div align="center">

**Made with ❤️ for the AI development community**

**🌐 [Try Web App](https://piyushiitk24.github.io/Offtoken/webapp.html) • 🔒 [Setup Locally](#local-setup) • ⭐ [Star this repo](https://github.com/Piyushiitk24/Offtoken)**

</div>
