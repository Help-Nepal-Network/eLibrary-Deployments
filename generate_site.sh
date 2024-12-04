#!/bin/bash
echo "eLibrary site generation started on " `date`
echo "creating virtual env..."
./venv/bin/python3 -m venv venv
echo "installing requirements..."
pip install -r requirements.txt
source venv/bin/activate
echo "generating site..."
./venv/bin/python3 generate_site.py