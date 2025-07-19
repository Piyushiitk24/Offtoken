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

def main():
    st.set_page_config(
        page_title="Token Counter Pro",
        page_icon="🔢",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    st.title("🔢 Token Counter Pro")
    st.markdown("**Professional token counting with real tokenizers**")
    
    # Initialize token counter
    @st.cache_resource
    def get_token_counter():
        return TokenCounter()
    
    token_counter = get_token_counter()
    available_tokenizers = token_counter.get_available_tokenizers()
    
    if not available_tokenizers:
        st.error("No tokenizers available. Please check your installation.")
        return
    
    # Sidebar configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Model selection
        selected_model = st.selectbox(
            "Select Tokenizer",
            options=list(available_tokenizers.keys()),
            format_func=lambda x: f"{x} - {available_tokenizers[x]}"
        )
        
        # Cost estimation
        st.subheader("💰 Cost Estimation")
        input_cost = st.number_input(
            "Input cost per 1K tokens ($)",
            min_value=0.0,
            value=0.0,
            step=0.001,
            format="%.6f"
        )
        output_cost = st.number_input(
            "Output cost per 1K tokens ($)",
            min_value=0.0,
            value=0.0,
            step=0.001,
            format="%.6f"
        )
        
        # Common pricing presets
        if st.button("GPT-4 Pricing"):
            st.session_state.input_cost = 0.03
            st.session_state.output_cost = 0.06
        
        if st.button("GPT-3.5 Pricing"):
            st.session_state.input_cost = 0.001
            st.session_state.output_cost = 0.002
    
    # Main interface
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📄 Input")
        
        # File upload
        uploaded_file = st.file_uploader(
            "Upload document",
            type=['txt', 'pdf', 'docx'],
            help="Supported: TXT, PDF, DOCX"
        )
        
        # Text input
        text_input = st.text_area(
            "Or paste text here",
            height=300,
            placeholder="Enter your text here..."
        )
    
    with col2:
        st.subheader("📊 Results")
        
        # Process input
        text = ""
        source = ""
        
        if uploaded_file:
            try:
                file_type = uploaded_file.name.split('.')[-1].lower()
                with st.spinner("Extracting text..."):
                    text = DocumentProcessor.extract_text(uploaded_file.getvalue(), file_type)
                source = uploaded_file.name
            except Exception as e:
                st.error(f"Error processing file: {e}")
                return
        
        elif text_input:
            text = text_input
            source = "Direct input"
        
        if text:
            try:
                # Count tokens
                with st.spinner("Counting tokens..."):
                    result = token_counter.count_tokens(text, selected_model)
                
                # Display results
                token_count = result['token_count']
                word_count = len(text.split())
                char_count = len(text)
                
                # Metrics
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    st.metric("Tokens", f"{token_count:,}")
                with col_b:
                    st.metric("Words", f"{word_count:,}")
                with col_c:
                    st.metric("Characters", f"{char_count:,}")
                
                # Cost calculation
                if input_cost > 0:
                    total_cost = (token_count / 1000) * input_cost
                    st.metric("Estimated Cost", f"${total_cost:.6f}")
                
                # Text preview
                with st.expander("📖 Text Preview"):
                    preview = text[:1000] + "..." if len(text) > 1000 else text
                    st.text_area("Content", preview, height=200, disabled=True)
                
                # Token analysis
                with st.expander("🔍 Token Analysis"):
                    st.write(f"**Model:** {selected_model}")
                    st.write(f"**Type:** {result['tokenizer_type']}")
                    st.write(f"**Source:** {source}")
                    
                    if 'tokens' in result:
                        st.write("**First 20 tokens:**")
                        first_tokens = result['tokens'][:20]
                        if result['tokenizer_type'] == 'tiktoken':
                            # Decode tiktoken tokens
                            tokenizer = token_counter.tokenizers[selected_model]
                            decoded = [tokenizer.decode([t]) for t in first_tokens]
                            st.code(str(decoded))
                        else:
                            st.code(str(first_tokens))
                
                # Export
                st.subheader("📥 Export")
                
                # Prepare export data
                export_data = {
                    'source': source,
                    'model': selected_model,
                    'tokens': token_count,
                    'words': word_count,
                    'characters': char_count,
                    'timestamp': pd.Timestamp.now().isoformat()
                }
                
                if input_cost > 0:
                    export_data['estimated_cost'] = total_cost
                
                # CSV export
                df = pd.DataFrame([export_data])
                csv = df.to_csv(index=False)
                st.download_button(
                    "📊 Download CSV",
                    csv,
                    f"tokens_{selected_model}_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    "text/csv"
                )
                
                # Text export
                export_text = f"""Token Count Report
==================

Source: {source}
Model: {selected_model}
Date: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}

RESULTS:
- Tokens: {token_count:,}
- Words: {word_count:,}
- Characters: {char_count:,}
"""
                if input_cost > 0:
                    export_text += f"- Estimated Cost: ${total_cost:.6f}\n"
                
                export_text += f"\nTEXT PREVIEW:\n{text[:500]}{'...' if len(text) > 500 else ''}"
                
                st.download_button(
                    "📄 Download TXT",
                    export_text,
                    f"tokens_{selected_model}_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    "text/plain"
                )
                
            except Exception as e:
                st.error(f"Error counting tokens: {e}")
                st.error(traceback.format_exc())
        
        else:
            st.info("👆 Upload a file or paste text to get started")
    
    # Footer
    st.markdown("---")
    st.markdown("**Note:** This tool uses authentic tokenizers from model providers. Token counts are accurate for API usage.")

if __name__ == "__main__":
    main()
