#!/bin/bash
python3 -m venv import
source import/bin/activate
pip install -r requirements.txt
streamlit run mainpage.py
