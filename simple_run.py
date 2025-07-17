#!/usr/bin/env python3
"""
Simple test script to verify everything works
"""

import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    print("🧪 Testing imports...")
    
    try:
        import gradio
        print("✅ Gradio imported successfully")
    except ImportError as e:
        print(f"❌ Gradio import failed: {e}")
        return False
    
    try:
        import crewai
        print("✅ CrewAI imported successfully")
    except ImportError as e:
        print(f"❌ CrewAI import failed: {e}")
        return False
    
    try:
        from src.stock_picker.crew import StockPicker
        print("✅ Stock Picker imported successfully")
    except ImportError as e:
        print(f"❌ Stock Picker import failed: {e}")
        return False
    
    print("🎉 All imports successful!")
    return True

def run_gradio():
    print("\n🚀 Starting Gradio app...")
    try:
        import gradio as gr
        from src.stock_picker.crew import StockPicker
        from datetime import datetime
        
        def run_stock_analysis(sector="Technology"):
            try:
                inputs = {
                    'sector': sector,
                    "current_date": str(datetime.now())
                }
                result = StockPicker().crew().kickoff(inputs=inputs)
                return f"\n\n=== FINAL DECISION ===\n\n{result.raw}"
            except Exception as e:
                return f"Error: {str(e)}"
        
        with gr.Blocks(title="Stock Picker AI") as demo:
            gr.Markdown("# 🚀 Stock Picker AI")
            with gr.Row():
                sector_input = gr.Textbox(label="Sector to Analyze", value="Technology")
                analyze_btn = gr.Button("🚀 Analyze Stocks", variant="primary")
            output = gr.Textbox(label="Analysis Result", lines=30, interactive=False)
            
            def analyze(sector):
                if not sector.strip():
                    return "Please enter a sector name."
                return run_stock_analysis(sector.strip())
            
            analyze_btn.click(analyze, inputs=[sector_input], outputs=[output])
        
        print("🌐 Opening browser to: http://localhost:7860")
        demo.launch(server_name="0.0.0.0", server_port=7860, share=True)
        
    except Exception as e:
        print(f"❌ Error starting Gradio: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Stock Picker AI - Simple Test")
    print("=" * 40)
    
    if test_imports():
        run_gradio()
    else:
        print("\n❌ Import test failed. Please check your setup.")
        sys.exit(1) 