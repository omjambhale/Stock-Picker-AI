#!/bin/bash

# Set Python path to include current directory
export PYTHONPATH=.

# Activate virtual environment
source .venv/bin/activate

# Install dependencies if needed
pip install -r requirements.txt

# Run the Gradio app
python gradio_app.py
