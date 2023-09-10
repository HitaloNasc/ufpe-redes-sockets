#!/bin/bash

# Delete the virtual environment if it exists
rm -rf venv

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
