# 🚀 Stock Picker AI Agent

An intelligent AI-powered stock analysis and recommendation system built with CrewAI. This agent analyzes market trends, company fundamentals, and financial data to provide informed stock investment recommendations.

## ✨ Features

- **🤖 AI-Powered Analysis**: Uses multiple AI agents to analyze different aspects of stock investment
- **📊 Market Research**: Comprehensive market trend analysis and company research
- **💡 Investment Recommendations**: Data-driven stock recommendations with reasoning
- **📈 Financial Analysis**: Deep dive into company fundamentals and financial metrics
- **🔄 Memory System**: Maintains context and learns from previous analyses
- **📋 Structured Output**: Generates detailed reports in markdown format

## 🏗️ Architecture

The project uses CrewAI's multi-agent system with specialized agents:

- **Research Agent**: Gathers market data and company information
- **Analysis Agent**: Performs financial analysis and trend evaluation
- **Recommendation Agent**: Synthesizes findings into actionable recommendations

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- OpenAI API key
- Polygon API key (for financial data)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd stock-picker-ai
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   # or using uv
   uv sync
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. **Run the stock picker**
   ```bash
   python -m stock_picker.main
   ```

## 📁 Project Structure

```
stock-picker-ai/
├── src/
│   └── stock_picker/
│       ├── __init__.py
│       ├── main.py              # Main entry point
│       ├── crew.py              # CrewAI configuration
│       ├── config/
│       │   ├── agents.yaml      # Agent definitions
│       │   └── tasks.yaml       # Task definitions
│       └── tools/
│           ├── __init__.py
│           └── push_tool.py     # Custom tools
├── knowledge/
│   └── user_preference.txt      # User preferences
├── memory/                      # AI memory storage
├── output/                      # Generated reports
├── pyproject.toml              # Project configuration
└── README.md                   # This file
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
OPENAI_API_KEY=your_openai_api_key
POLYGON_API_KEY=your_polygon_api_key
SERPER_API_KEY=your_serper_api_key  # Optional
```

### Agent Configuration

Modify `src/stock_picker/config/agents.yaml` to customize agent behavior:

```yaml
research_agent:
  name: "Market Research Specialist"
  role: "Gather comprehensive market and company data"
  goal: "Provide accurate and up-to-date market information"

analysis_agent:
  name: "Financial Analyst"
  role: "Analyze financial metrics and trends"
  goal: "Evaluate investment potential and risks"
```

## 📊 Usage Examples

### Basic Stock Analysis

```python
from stock_picker.main import run_stock_analysis

# Analyze a specific stock
result = run_stock_analysis("AAPL")
print(result)
```

### Market Research

```python
from stock_picker.crew import StockPickerCrew

crew = StockPickerCrew()
result = crew.kickoff(inputs={"research_type": "market_trends"})
```

## 📈 Output Format

The system generates structured reports including:

- **Market Analysis**: Current market conditions and trends
- **Company Overview**: Business model and competitive position
- **Financial Metrics**: Key ratios and performance indicators
- **Risk Assessment**: Potential risks and challenges
- **Recommendation**: Buy/Hold/Sell recommendation with reasoning

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [CrewAI](https://github.com/joaomdmoura/crewAI) for the multi-agent framework
- [OpenAI](https://openai.com/) for the AI models
- [Polygon](https://polygon.io/) for financial data

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/your-username/stock-picker-ai/issues) page
2. Create a new issue with detailed information
3. Join our community discussions

---

**Disclaimer**: This tool is for educational and research purposes only. Investment decisions should be made after consulting with qualified financial advisors. Past performance does not guarantee future results.
