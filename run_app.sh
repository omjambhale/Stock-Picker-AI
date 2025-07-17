#!/bin/bash

# Set Python path to current directory (same as gradio_app.py does)
export PYTHONPATH=.

# Activate virtual environment
source .venv/bin/activate

# Install gradio if not already installed
pip install gradio

# Run the Gradio app (which works exactly like main.py)
python gradio_app.py
