#!/usr/bin/env python
import sys
import warnings
import os
import gradio as gr
from datetime import datetime

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the same way as main.py
from src.stock_picker.crew import StockPicker

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run_stock_analysis(sector="Technology"):
    """
    Run the research crew - exactly like main.py does
    """
    try:
        inputs = {
            'sector': sector,
            "current_date": str(datetime.now())
        }

        # Create and run the crew - exactly like main.py
        result = StockPicker().crew().kickoff(inputs=inputs)
        
        # Return the result - exactly like main.py prints
        return f"\n\n=== FINAL DECISION ===\n\n{result.raw}"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    with gr.Blocks(title="Stock Picker AI", theme=gr.themes.Soft()) as demo:
        gr.Markdown("""
        # 🚀 Stock Picker AI
        
        **Enter a sector to analyze stocks using AI agents**
        """)
        
        with gr.Row():
            sector_input = gr.Textbox(
                label="Sector to Analyze", 
                value="Technology",
                placeholder="e.g., Technology, Healthcare, Finance..."
            )
            analyze_btn = gr.Button("🚀 Analyze Stocks", variant="primary")
        
        output = gr.Textbox(
            label="Analysis Result", 
            lines=30, 
            interactive=False,
            show_copy_button=True
        )
        
        def analyze(sector):
            if not sector.strip():
                return "Please enter a sector name."
            return run_stock_analysis(sector.strip())
        
        analyze_btn.click(
            analyze,
            inputs=[sector_input],
            outputs=[output]
        )

    print("🚀 Starting Stock Picker AI with Gradio interface...")
    demo.launch(server_name="0.0.0.0", server_port=7860, share=True)

if __name__ == "__main__":
    main()
