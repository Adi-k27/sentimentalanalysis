# Sentiment & Discrimination Analysis Dashboard

This project is an interactive dashboard built with Streamlit for analyzing government employee survey data related to harassment, discrimination, and sentiment scoring.

---

## Features

- Trend analysis for harassment and discrimination questions (Q57–Q58, Q65–Q66)
- Gender-based filters (e.g., women for Q57–Q58, men for Q65–Q66)
- Sentiment classification: Positive, Neutral, Negative
- Sidebar navigation for seamless switching between analysis views
- Expandable section to preview raw data

---

## Folder Structure

sentiment_analysis_app/
│
├── app.py                          # Main Streamlit app
│
├── utils/
│   ├── __init__.py
│   ├── data_loader.py                 # Dataset loading
│   ├── sentiment.py                   # Sentiment bucketing logic
│   ├── q57_q63_analysis.py            # Harassment by women
│   └── q65_q66_analysis.py            # Discrimination types (men)
│
├── requirements.txt               # Dependencies
└── README.md                      # Project overview

## Setup Instructions

1. Clone or download this repository.
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt

## Setup Instructions

   streamlit run app.py

## Data Requirements

data/cleaned/Cleaned Subset 3.csv

## Requirements

Python 3.8 or higher
Libraries: pandas, plotly, streamlit

## Author
Vasanth Gnana Seelan
https://github.com/vasanthgnanaseelan

