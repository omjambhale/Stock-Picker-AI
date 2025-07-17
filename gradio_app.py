import os
import gradio as gr
from src.stock_picker.crew import StockPicker
from datetime import datetime

def ensure_output_dir():
    os.makedirs('output', exist_ok=True)

def run_stock_analysis(sector="Technology"):
    ensure_output_dir()
    try:
        inputs = {
            'sector': sector,
            "current_date": str(datetime.now())
        }
        result = StockPicker().crew().kickoff(inputs=inputs)
        filename = f"output/{sector.replace(' ', '_')}_stock_analysis.md"
        with open(filename, 'w') as f:
            f.write(result.raw)
        return result.raw, filename, None
    except Exception as e:
        return None, None, str(e)

def gradio_interface(sector):
    if not sector.strip():
        return gr.update(value="", visible=True), None, "Please enter a sector name."
    report, filename, error = run_stock_analysis(sector.strip())
    if error:
        return gr.update(value="", visible=True), None, f"Error: {error}"
    return report, filename, None

def download_report(filename):
    if filename and os.path.exists(filename):
        return filename
    return None

def main():
    with gr.Blocks(title="Stock Picker AI Assistant", theme=gr.themes.Soft()) as demo:
        gr.Markdown("# 🚀 Stock Picker AI Assistant")
        with gr.Row():
            sector_input = gr.Textbox(label="Sector to Analyze", value="Technology")
            run_btn = gr.Button("Analyze Stocks", variant="primary")
        output = gr.Textbox(label="Stock Analysis Report", lines=20, interactive=False)
        download_btn = gr.DownloadButton("Download Report", visible=False)
        error_box = gr.Markdown(visible=False)
        
        def on_run(sector):
            report, filename, error = gradio_interface(sector)
            if error:
                return "", gr.update(visible=False), gr.update(visible=True, value=f"Error: {error}")
            return report, gr.update(visible=True, value=filename), gr.update(visible=False)

        run_btn.click(on_run, inputs=[sector_input], outputs=[output, download_btn, error_box])
        download_btn.click(download_report, inputs=[download_btn], outputs=None)

    print("Starting Gradio app...")
    demo.launch(server_name="0.0.0.0", server_port=7860, share=True)

if __name__ == "__main__":
    main()
