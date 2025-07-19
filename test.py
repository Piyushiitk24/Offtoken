#!/usr/bin/env python3
"""Test the tokenizer functionality"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import TokenCounter

def test_tokenizers():
    print("🔢 Testing Token Counter Pro")
    print("=" * 40)
    
    # Initialize token counter
    counter = TokenCounter()
    available = counter.get_available_tokenizers()
    
    print(f"Available tokenizers: {len(available)}")
    for name, desc in available.items():
        print(f"  • {name}: {desc}")
    
    # Test with sample text
    sample_text = "Hello, world! This is a test of the tokenization system."
    
    print(f"\nTesting with: '{sample_text}'")
    print("-" * 40)
    
    for model_name in available.keys():
        try:
            result = counter.count_tokens(sample_text, model_name)
            print(f"{model_name:20}: {result['token_count']:3} tokens")
        except Exception as e:
            print(f"{model_name:20}: Error - {e}")
    
    print("\n✅ Test completed!")

if __name__ == "__main__":
    test_tokenizers()
