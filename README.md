Stock Picker AI

An intelligent AI-powered stock analysis and recommendation system built with CrewAI. This agent analyzes market trends, company fundamentals, and financial data to provide informed stock investment recommendations.

## ✨ Features

- ** AI-Powered Analysis**: Uses multiple AI agents to analyze different aspects of stock investment
- ** Market Research**: Comprehensive market trend analysis and company research
- ** Investment Recommendations**: Data-driven stock recommendations with reasoning
- ** Financial Analysis**: Deep dive into company fundamentals and financial metrics
- ** Memory System**: Maintains context and learns from previous analyses
- ** Web Interface**: Beautiful Gradio web interface for easy interaction

##  Quick Start

### Prerequisites

- Python 3.10+
- OpenAI API key

### Installation & Usage

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd stock-picker-ai
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your OpenAI API key
   ```

3. **Run the web interface**
   ```bash
   chmod +x run_app.sh
   ./run_app.sh
   ```

4. **Or run manually**
   ```bash
   source .venv/bin/activate
   export PYTHONPATH=.
   pip install gradio
   python gradio_app.py
   ```

5. **Open your browser**
   Go to `http://localhost:7860`

## 🎯 How It Works

The Gradio interface works **exactly** like the original command-line stock_picker:

1. **Input**: Enter a sector (e.g., "Technology", "Healthcare", "Finance")
2. **Processing**: The same AI agents analyze the sector (no changes to the core logic)
3. **Output**: Same detailed analysis report, just displayed in a nice web interface

**The core functionality is identical** - we just added a UI layer on top!

## 📁 Project Structure

```
stock-picker-ai/
├── src/stock_picker/          # Original stock picker code (unchanged)
│   ├── config/               # Agent and task configurations
│   ├── tools/                # Custom tools and utilities
│   ├── crew.py              # Main crew definition
│   └── main.py              # Original command-line entry point
├── gradio_app.py            # Web interface (works like main.py)
├── run_app.sh               # Simple startup script
├── requirements.txt         # Minimal dependencies
└── README.md               # This file
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file with:
```env
OPENAI_API_KEY=your_openai_api_key
```

## 📊 Usage Examples

### Web Interface (Recommended)
1. Run `./run_app.sh`
2. Open browser to `http://localhost:7860`
3. Enter sector (e.g., "Technology")
4. Click "Analyze Stocks"
5. View the same detailed analysis you'd get from command line

### Command Line (Original)
```bash
python -m src.stock_picker.main
```
