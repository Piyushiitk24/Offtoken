import streamlit as st
import pandas as pd
import tempfile
import os
from pathlib import Path
import logging
from typing import Dict, Any, Optional
import traceback

# Document processing
import pdfplumber
from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import docx
import re

# Tokenizers
import tiktoken
# from transformers import AutoTokenizer  # Disabled for stability
# from anthropic import Anthropic  # Disabled for stability

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TokenCounter:
    """Professional token counter with proper tokenizer implementations"""
    
    def __init__(self):
        self.tokenizers = {}
        self._initialize_tokenizers()
    
    def _initialize_tokenizers(self):
        """Initialize all available tokenizers"""
        try:
            # OpenAI tokenizers (tiktoken)
            self.tokenizers['gpt-4'] = tiktoken.encoding_for_model('gpt-4')
            self.tokenizers['gpt-3.5-turbo'] = tiktoken.encoding_for_model('gpt-3.5-turbo')
            self.tokenizers['text-davinci-003'] = tiktoken.encoding_for_model('text-davinci-003')
            
            # Backup encodings
            self.tokenizers['cl100k_base'] = tiktoken.get_encoding('cl100k_base')  # GPT-4, GPT-3.5
            self.tokenizers['p50k_base'] = tiktoken.get_encoding('p50k_base')      # GPT-3, Codex
            
        except Exception as e:
            logger.warning(f"Failed to initialize tiktoken: {e}")
        
        # Hugging Face tokenizers (disabled for stability on Python 3.13)
        # Will be enabled when compatibility is confirmed
        """
        hf_models = {
            'llama2-7b': 'meta-llama/Llama-2-7b-hf',
            'llama2-13b': 'meta-llama/Llama-2-13b-hf',
            'mistral-7b': 'mistralai/Mistral-7B-v0.1',
            'gemma-7b': 'google/gemma-7b',
            'falcon-7b': 'tiiuae/falcon-7b',
            'code-llama': 'codellama/CodeLlama-7b-hf',
        }
        
        for name, model_id in hf_models.items():
            try:
                from transformers import AutoTokenizer
                self.tokenizers[name] = AutoTokenizer.from_pretrained(
                    model_id, 
                    trust_remote_code=True,
                    use_fast=True
                )
                logger.info(f"Loaded tokenizer: {name}")
            except Exception as e:
                logger.warning(f"Failed to load {name}: {e}")
        """
    
    def get_available_tokenizers(self) -> Dict[str, str]:
        """Get list of available tokenizers with descriptions"""
        descriptions = {
            'gpt-4': 'OpenAI GPT-4 (most accurate for GPT-4 API)',
            'gpt-3.5-turbo': 'OpenAI GPT-3.5 Turbo (ChatGPT)',
            'text-davinci-003': 'OpenAI GPT-3 (text-davinci-003)',
            'cl100k_base': 'OpenAI cl100k_base (GPT-4, GPT-3.5)',
            'p50k_base': 'OpenAI p50k_base (GPT-3, Codex)',
            # HF models disabled for stability
            # 'llama2-7b': 'Meta Llama 2 7B',
            # 'llama2-13b': 'Meta Llama 2 13B',
            # 'mistral-7b': 'Mistral 7B',
            # 'gemma-7b': 'Google Gemma 7B',
            # 'falcon-7b': 'Falcon 7B',
            # 'code-llama': 'Meta Code Llama 7B',
        }
        
        return {k: v for k, v in descriptions.items() if k in self.tokenizers}
    
    def count_tokens(self, text: str, model_name: str) -> Dict[str, Any]:
        """Count tokens using the specified model"""
        if model_name not in self.tokenizers:
            raise ValueError(f"Tokenizer {model_name} not available")
        
        tokenizer = self.tokenizers[model_name]
        
        try:
            if hasattr(tokenizer, 'encode'):
                if isinstance(tokenizer, tiktoken.Encoding):
                    # tiktoken tokenizer
                    tokens = tokenizer.encode(text)
                    return {
                        'token_count': len(tokens),
                        'tokens': tokens[:100],  # First 100 tokens for preview
                        'tokenizer_type': 'tiktoken'
                    }
                else:
                    # Hugging Face tokenizer
                    encoding = tokenizer.encode(text)
                    return {
                        'token_count': len(encoding),
                        'tokens': encoding[:100],  # First 100 tokens for preview
                        'tokenizer_type': 'huggingface'
                    }
            else:
                raise ValueError(f"Invalid tokenizer type for {model_name}")
        except Exception as e:
            logger.error(f"Error counting tokens with {model_name}: {e}")
            raise

class DocumentProcessor:
    """Handle document text extraction"""
    
    @staticmethod
    def extract_text(file_bytes: bytes, file_type: str) -> str:
        """Extract text from various document types"""
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_type}") as tmp_file:
            tmp_file.write(file_bytes)
            file_path = tmp_file.name
        
        try:
            if file_type == 'txt':
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    return f.read()
            
            elif file_type == 'pdf':
                # Try text extraction first
                text = ""
                with pdfplumber.open(file_path) as pdf:
                    for page in pdf.pages:
                        page_text = page.extract_text()
                        if page_text:
                            text += page_text + "\n"
                
                # If no text found, use OCR
                if not text.strip():
                    st.info("No text found in PDF. Using OCR...")
                    images = convert_from_path(file_path)
                    ocr_text = []
                    for i, img in enumerate(images):
                        with st.spinner(f"Processing page {i+1}/{len(images)}..."):
                            page_text = pytesseract.image_to_string(img, lang='eng')
                            ocr_text.append(page_text)
                    text = "\n".join(ocr_text)
                
                return text
            
            elif file_type == 'docx':
                doc = docx.Document(file_path)
                paragraphs = [para.text for para in doc.paragraphs]
                return "\n".join(paragraphs)
            
            else:
                raise ValueError(f"Unsupported file type: {file_type}")
        
        finally:
            if os.path.exists(file_path):
                os.unlink(file_path)

def apply_custom_css():
    """Apply custom CSS with subtle PRIDE-themed colors"""
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Root variables with subtle PRIDE theme */
    :root {
        --pride-red: #FF6B9D;
        --pride-orange: #FFB347;
        --pride-yellow: #FFE066;
        --pride-green: #90EE90;
        --pride-blue: #87CEEB;
        --pride-purple: #DDA0DD;
        
        --bg-primary: #FAFBFC;
        --bg-secondary: #F8F9FA;
        --bg-accent: linear-gradient(135deg, #FF6B9D15, #87CEEB15);
        --text-primary: #2D3748;
        --text-secondary: #718096;
        --border-color: #E2E8F0;
        --shadow-soft: 0 4px 12px rgba(0, 0, 0, 0.05);
        --shadow-medium: 0 8px 25px rgba(0, 0, 0, 0.1);
    }
    
    /* Hide Streamlit branding and menu */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Global font family */
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Main container styling */
    .main > div {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Custom header with gradient */
    .hero-header {
        background: linear-gradient(135deg, 
            var(--pride-red)20, 
            var(--pride-orange)20, 
            var(--pride-yellow)20, 
            var(--pride-green)20, 
            var(--pride-blue)20, 
            var(--pride-purple)20);
        padding: 2rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        text-align: center;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .hero-title {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, var(--pride-red), var(--pride-blue));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
        color: var(--text-secondary);
        font-weight: 400;
        margin: 0;
    }
    
    /* Enhanced cards */
    .custom-card {
        background: var(--bg-secondary);
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: var(--shadow-soft);
        border: 1px solid var(--border-color);
        transition: all 0.3s ease;
        margin-bottom: 1rem;
    }
    
    .custom-card:hover {
        box-shadow: var(--shadow-medium);
        transform: translateY(-2px);
    }
    
    /* Metric cards with PRIDE colors */
    .metric-card {
        background: linear-gradient(135deg, var(--bg-primary), var(--bg-secondary));
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: var(--shadow-soft);
        border: 1px solid var(--border-color);
        position: relative;
        overflow: hidden;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, 
            var(--pride-red), 
            var(--pride-orange), 
            var(--pride-yellow), 
            var(--pride-green), 
            var(--pride-blue), 
            var(--pride-purple));
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 0.5rem;
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: var(--text-secondary);
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-weight: 500;
    }
    
    /* Enhanced sidebar */
    .css-1d391kg {
        background: var(--bg-secondary);
        border-right: 1px solid var(--border-color);
    }
    
    /* Buttons with PRIDE theme */
    .stButton > button {
        background: linear-gradient(135deg, var(--pride-red), var(--pride-blue));
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 500;
        transition: all 0.3s ease;
        box-shadow: var(--shadow-soft);
    }
    
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: var(--shadow-medium);
        opacity: 0.9;
    }
    
    /* File uploader styling */
    .uploadedFile {
        border: 2px dashed var(--pride-blue);
        border-radius: 12px;
        padding: 2rem;
        text-align: center;
        background: var(--bg-accent);
        transition: all 0.3s ease;
    }
    
    /* Progress bars */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, 
            var(--pride-red), 
            var(--pride-orange), 
            var(--pride-yellow), 
            var(--pride-green));
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: var(--bg-accent);
        border-radius: 8px;
        border: 1px solid var(--border-color);
    }
    
    /* Text areas and inputs */
    .stTextArea textarea, .stTextInput input {
        border-radius: 8px;
        border: 1px solid var(--border-color);
        font-family: 'Inter', monospace;
    }
    
    /* Selectbox styling */
    .stSelectbox > div > div {
        border-radius: 8px;
        border: 1px solid var(--border-color);
    }
    
    /* Number input styling */
    .stNumberInput input {
        border-radius: 8px;
        border: 1px solid var(--border-color);
    }
    
    /* Custom info boxes */
    .info-box {
        background: linear-gradient(135deg, var(--pride-blue)15, var(--pride-green)15);
        border-left: 4px solid var(--pride-blue);
        padding: 1rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
    }
    
    .success-box {
        background: linear-gradient(135deg, var(--pride-green)15, var(--pride-yellow)15);
        border-left: 4px solid var(--pride-green);
        padding: 1rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
    }
    
    .warning-box {
        background: linear-gradient(135deg, var(--pride-orange)15, var(--pride-red)15);
        border-left: 4px solid var(--pride-orange);
        padding: 1rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
    }
    
    /* Footer */
    .custom-footer {
        margin-top: 3rem;
        padding: 2rem;
        text-align: center;
        background: var(--bg-accent);
        border-radius: 12px;
        border: 1px solid var(--border-color);
    }
    
    /* Animations */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .fade-in {
        animation: fadeInUp 0.6s ease-out;
    }
    
    /* Dark mode support */
    @media (prefers-color-scheme: dark) {
        :root {
            --bg-primary: #1A202C;
            --bg-secondary: #2D3748;
            --text-primary: #F7FAFC;
            --text-secondary: #CBD5E0;
            --border-color: #4A5568;
        }
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.set_page_config(
        page_title="TokenForge - Professional Token Counter",
        page_icon="✨",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://github.com/Piyushiitk24/Offtoken',
            'Report a bug': 'https://github.com/Piyushiitk24/Offtoken/issues',
            'About': """
            # TokenForge ✨
            Professional token counting with authentic tokenizers.
            Built with love for developers, researchers, and AI enthusiasts.
            """
        }
    )
    
    # Apply custom CSS
    apply_custom_css()
    
    # Hero Section
    st.markdown("""
    <div class="hero-header fade-in">
        <h1 class="hero-title">✨ TokenForge</h1>
        <p class="hero-subtitle">Professional token counting with authentic tokenizers</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize token counter
    @st.cache_resource
    def get_token_counter():
        return TokenCounter()
    
    token_counter = get_token_counter()
    available_tokenizers = token_counter.get_available_tokenizers()
    
    if not available_tokenizers:
        st.error("No tokenizers available. Please check your installation.")
        return
    
    # Sidebar configuration with enhanced styling
    with st.sidebar:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown("### ⚙️ Configuration")
        
        # Model selection with enhanced description
        selected_model = st.selectbox(
            "🤖 Select Tokenizer",
            options=list(available_tokenizers.keys()),
            format_func=lambda x: f"{x} - {available_tokenizers[x]}",
            help="Choose the tokenizer that matches your target model"
        )
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Cost estimation section
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown("### 💰 Cost Estimation")
        
        col_cost1, col_cost2 = st.columns(2)
        with col_cost1:
            input_cost = st.number_input(
                "Input ($/1K tokens)",
                min_value=0.0,
                value=0.0,
                step=0.001,
                format="%.6f",
                help="Cost per 1000 input tokens"
            )
        with col_cost2:
            output_cost = st.number_input(
                "Output ($/1K tokens)",
                min_value=0.0,
                value=0.0,
                step=0.001,
                format="%.6f",
                help="Cost per 1000 output tokens"
            )
        
        # Pricing presets with enhanced buttons
        st.markdown("#### 🎯 Quick Presets")
        col_preset1, col_preset2 = st.columns(2)
        
        with col_preset1:
            if st.button("GPT-4", help="Set GPT-4 pricing", use_container_width=True):
                st.session_state.input_cost = 0.03
                st.session_state.output_cost = 0.06
                st.rerun()
        
        with col_preset2:
            if st.button("GPT-3.5", help="Set GPT-3.5 pricing", use_container_width=True):
                st.session_state.input_cost = 0.001
                st.session_state.output_cost = 0.002
                st.rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Feature highlights
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown("### ✨ Features")
        features = [
            "🎯 **Authentic Tokenizers** - Real OpenAI tiktoken",
            "📄 **Multi-Format Support** - PDF, DOCX, TXT",
            "🔍 **OCR Processing** - Scanned document support", 
            "💰 **Cost Calculation** - Accurate API pricing",
            "📊 **Detailed Analytics** - Token breakdown",
            "📥 **Export Options** - CSV and TXT formats"
        ]
        
        for feature in features:
            st.markdown(feature)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Main interface with enhanced layout
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.markdown('<div class="custom-card fade-in">', unsafe_allow_html=True)
        st.markdown("### 📄 Input Source")
        
        # Enhanced file upload
        uploaded_file = st.file_uploader(
            "📎 Upload Document",
            type=['txt', 'pdf', 'docx'],
            help="Supported formats: TXT, PDF, DOCX (including scanned PDFs with OCR)",
            label_visibility="collapsed"
        )
        
        if uploaded_file:
            st.markdown(f"""
            <div class="success-box">
                <strong>📎 File Uploaded:</strong> {uploaded_file.name}<br>
                <strong>📏 Size:</strong> {uploaded_file.size:,} bytes<br>
                <strong>🔧 Type:</strong> {uploaded_file.type}
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("**OR**")
        
        # Enhanced text input
        text_input = st.text_area(
            "✏️ Paste Your Text",
            height=300,
            placeholder="Enter or paste your text here...\n\nTip: You can paste content from articles, code, documentation, or any text you want to analyze for token count.",
            help="Direct text input for quick analysis"
        )
        
        # Input stats
        if text_input:
            char_count = len(text_input)
            word_count = len(text_input.split())
            line_count = len(text_input.split('\n'))
            
            st.markdown(f"""
            <div class="info-box">
                <strong>📊 Input Statistics:</strong><br>
                Characters: {char_count:,} | Words: {word_count:,} | Lines: {line_count:,}
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="custom-card fade-in">', unsafe_allow_html=True)
        st.markdown("### 📊 Analysis Results")
        
        # Process input
        text = ""
        source = ""
        total_cost = 0.0  # Initialize to prevent unbound variable error
        
        if uploaded_file:
            try:
                file_type = uploaded_file.name.split('.')[-1].lower()
                with st.spinner("🔄 Extracting text from document..."):
                    text = DocumentProcessor.extract_text(uploaded_file.getvalue(), file_type)
                source = uploaded_file.name
                st.success(f"✅ Successfully extracted text from {uploaded_file.name}")
            except Exception as e:
                st.error(f"❌ Error processing file: {e}")
                st.markdown("</div>", unsafe_allow_html=True)
                return
        
        elif text_input:
            text = text_input
            source = "Direct input"
        
        if text:
            try:
                # Count tokens with loading animation
                with st.spinner("🧮 Analyzing tokens..."):
                    result = token_counter.count_tokens(text, selected_model)
                
                # Display results with enhanced metrics
                token_count = result['token_count']
                word_count = len(text.split())
                char_count = len(text)
                
                # Enhanced metrics display
                st.markdown("#### 📈 Token Analysis")
                
                metric_col1, metric_col2, metric_col3 = st.columns(3)
                
                with metric_col1:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-value">{token_count:,}</div>
                        <div class="metric-label">Tokens</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with metric_col2:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-value">{word_count:,}</div>
                        <div class="metric-label">Words</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with metric_col3:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-value">{char_count:,}</div>
                        <div class="metric-label">Characters</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Cost calculation with enhanced display
                if input_cost > 0:
                    total_cost = (token_count / 1000) * input_cost
                    st.markdown(f"""
                    <div class="metric-card" style="margin-top: 1rem;">
                        <div class="metric-value">${total_cost:.6f}</div>
                        <div class="metric-label">Estimated Cost</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Token efficiency ratio
                if word_count > 0:
                    token_per_word = token_count / word_count
                    st.markdown(f"""
                    <div class="info-box">
                        <strong>🎯 Efficiency Ratio:</strong> {token_per_word:.2f} tokens per word<br>
                        <strong>🔬 Model:</strong> {selected_model}<br>
                        <strong>📝 Source:</strong> {source}
                    </div>
                    """, unsafe_allow_html=True)
                
                # Text preview with enhanced styling
                with st.expander("📖 Text Preview", expanded=False):
                    preview = text[:2000] + "..." if len(text) > 2000 else text
                    st.markdown(f"""
                    <div style="background: var(--bg-primary); padding: 1rem; border-radius: 8px; border: 1px solid var(--border-color); font-family: 'Inter', monospace; max-height: 300px; overflow-y: auto;">
                        {preview.replace('\n', '<br>')}
                    </div>
                    """, unsafe_allow_html=True)
                
                # Token analysis with enhanced display
                with st.expander("🔍 Token Analysis", expanded=False):
                    analysis_col1, analysis_col2 = st.columns(2)
                    
                    with analysis_col1:
                        st.markdown(f"""
                        **🤖 Model Information:**
                        - **Tokenizer:** {selected_model}
                        - **Type:** {result['tokenizer_type']}
                        - **Source:** {source}
                        """)
                    
                    with analysis_col2:
                        st.markdown(f"""
                        **📊 Statistics:**
                        - **Token Density:** {(token_count/char_count)*100:.1f}% of characters
                        - **Compression Ratio:** {char_count/token_count:.1f}:1
                        - **Processing:** ✅ Complete
                        """)
                    
                    if 'tokens' in result and len(result['tokens']) > 0:
                        st.markdown("**🔤 First 20 Tokens Preview:**")
                        first_tokens = result['tokens'][:20]
                        if result['tokenizer_type'] == 'tiktoken':
                            # Decode tiktoken tokens
                            tokenizer = token_counter.tokenizers[selected_model]
                            decoded = [tokenizer.decode([t]).replace('\n', '\\n') for t in first_tokens]
                            
                            # Display tokens in a nice format
                            token_display = " | ".join([f"`{token}`" for token in decoded])
                            st.markdown(f"<div style='font-family: monospace; padding: 1rem; background: var(--bg-accent); border-radius: 8px; overflow-x: auto;'>{token_display}</div>", unsafe_allow_html=True)
                        else:
                            st.code(str(first_tokens))
                
                st.markdown("</div>", unsafe_allow_html=True)
                
                # Export section with enhanced styling
                st.markdown('<div class="custom-card fade-in">', unsafe_allow_html=True)
                st.markdown("### 📥 Export Results")
                
                # Prepare export data
                export_data = {
                    'source': source,
                    'model': selected_model,
                    'tokens': token_count,
                    'words': word_count,
                    'characters': char_count,
                    'timestamp': pd.Timestamp.now().isoformat(),
                    'token_per_word_ratio': round(token_count / word_count if word_count > 0 else 0, 3)
                }
                
                if input_cost > 0:
                    export_data['estimated_cost'] = total_cost
                    export_data['cost_per_token'] = input_cost / 1000
                
                # Enhanced export buttons
                export_col1, export_col2 = st.columns(2)
                
                with export_col1:
                    # CSV export
                    df = pd.DataFrame([export_data])
                    csv = df.to_csv(index=False)
                    st.download_button(
                        "📊 Download CSV Report",
                        csv,
                        f"tokenforge_analysis_{selected_model}_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv",
                        "text/csv",
                        help="Download detailed analysis as CSV file",
                        use_container_width=True
                    )
                
                with export_col2:
                    # Text export with enhanced format
                    export_text = f"""TokenForge Analysis Report
{'='*40}

📊 ANALYSIS SUMMARY
Source: {source}
Model: {selected_model}
Analyzed: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}

📈 RESULTS
• Tokens: {token_count:,}
• Words: {word_count:,}
• Characters: {char_count:,}
• Token/Word Ratio: {token_count / word_count if word_count > 0 else 0:.3f}
"""
                    if input_cost > 0:
                        export_text += f"• Estimated Cost: ${total_cost:.6f}\n• Cost per Token: ${input_cost/1000:.8f}\n"
                    
                    export_text += f"""
🔍 TECHNICAL DETAILS
• Tokenizer Type: {result['tokenizer_type']}
• Model: {selected_model}
• Processing: Complete

📝 TEXT PREVIEW
{'-'*20}
{text[:500]}{'...' if len(text) > 500 else ''}

---
Generated by TokenForge ✨
Professional Token Analysis Tool
"""
                    
                    st.download_button(
                        "📄 Download TXT Report",
                        export_text,
                        f"tokenforge_report_{selected_model}_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        "text/plain",
                        help="Download comprehensive report as text file",
                        use_container_width=True
                    )
                
                st.markdown("</div>", unsafe_allow_html=True)
                
            except Exception as e:
                st.markdown(f"""
                <div class="warning-box">
                    <strong>❌ Error analyzing tokens:</strong><br>
                    {str(e)}<br><br>
                    Please try with a different model or check your input text.
                </div>
                """, unsafe_allow_html=True)
                st.error(traceback.format_exc())
        
        else:
            # Enhanced empty state
            st.markdown("""
            <div class="info-box" style="text-align: center; padding: 3rem;">
                <h3>� Ready to Analyze!</h3>
                <p>Upload a document or paste text to get started with professional token analysis.</p>
                <br>
                <p><strong>✨ Pro Tips:</strong></p>
                <p>• Use the model selector to match your target API<br>
                • Set pricing for accurate cost estimates<br>
                • Export results for record keeping</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Enhanced footer
    st.markdown("""
    <div class="custom-footer fade-in">
        <h4>✨ TokenForge - Professional Token Analysis</h4>
        <p>Built with authentic tokenizers for accurate API cost estimation and context management.</p>
        <p>
            <strong>🔒 Privacy First:</strong> All processing happens locally • No data collection • Secure & Fast<br>
            <strong>🎯 Enterprise Ready:</strong> Production-grade tokenizers • Accurate results • Export capabilities
        </p>
        <hr style="margin: 1rem 0; border: none; height: 1px; background: linear-gradient(90deg, transparent, var(--pride-blue), transparent);">
        <p style="margin: 0; opacity: 0.7;">
            Made with 💖 for developers, researchers, and AI enthusiasts everywhere
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
