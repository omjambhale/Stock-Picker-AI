#!/bin/bash

echo "🚀 Starting Stock Picker AI..."

# Set Python path to current directory
export PYTHONPATH=.

# Activate virtual environment
source .venv/bin/activate

# Install only gradio (crewai is already installed)
pip install gradio

# Run the simple test script
python simple_run.py
