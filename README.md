# Sentiment Analysis of Public Sector Employee Feedback Survey

![Python](https://img.shields.io/badge/Python-3.9-blue.svg)  
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)  
![PowerBI](https://img.shields.io/badge/PowerBI-Dashboard-yellow.svg)  
![License](https://img.shields.io/badge/License-MIT-green.svg)  

This project analyzes **employee sentiment data** to uncover workplace trends around inclusion, psychological safety, and respect. It combines **NLP modeling, interactive apps, and visual dashboards** to make complex survey data accessible for both analysts and decision-makers.  

---

## Features  
- **Data Preprocessing & Modeling**: Jupyter notebooks for cleaning, feature engineering, and training sentiment models.  
- **Model Deployment**: Streamlit app (`/sentiment_analysis_app`) for interactive sentiment scoring and subgroup comparisons.  
- **Visualization**: Power BI dashboards with filters for department, identity groups (e.g., gender, 2SLGBTQIA+), and time.  
- **Reproducibility**: Source code in `/src` and trained artifacts in `/models`.  
- **Reports**: Project documentation, methodology, and findings stored in `/reports`.  

---

## Repository Structure  
```
sentimentalanalysis/
│
├── data/                   # Raw and processed survey datasets
├── models/                 # Trained models and vectorizers
├── notebooks/              # Jupyter notebooks for EDA, training, and evaluation
├── powerbi/                # Power BI report files (.pbix / visuals)
├── reports/                # Reports and documentation
├── sentiment_analysis_app/  # Streamlit app for live sentiment exploration
├── src/                    # Core Python modules (preprocessing, training, evaluation)
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│   └── ...
├── requirements.txt        # Python dependencies
├── ProjectInfo.txt         # Project description and context
└── README.md               # You are here
```

---

## Installation  

1. **Clone the repo**  
   ```bash
   git clone https://github.com/Adi-k27/sentimentalanalysis.git
   cd sentimentalanalysis
   ```

2. **Set up virtual environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate     # On Linux/Mac
   venv\Scripts\activate        # On Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage  

### 1. Run Jupyter Notebooks  
Explore preprocessing, model training, and evaluation.  
```bash
jupyter notebook
```

### 2. Launch Streamlit App  
Test predictions interactively.  
```bash
cd sentiment_analysis_app
streamlit run app.py
```

### 3. Open Power BI Dashboard  
Load `/powerbi/sentiment_dashboard.pbix` in Power BI Desktop to explore department- and identity-level insights.  

---

## Example Workflow  
1. Clean and preprocess raw survey data (`/notebooks/01_preprocessing.ipynb`).  
2. Train sentiment models (`/notebooks/02_modeling.ipynb`).  
3. Save best model and vectorizer to `/models`.  
4. Use Streamlit app for live text analysis and subgroup comparisons.  
5. Share results via Power BI dashboard and `/reports`.  

---

## Tech Stack  
- **Languages**: Python (scikit-learn, pandas, nltk/spacy, streamlit)  
- **Visualization**: Power BI, matplotlib/seaborn  
- **Data Science**: Jupyter Notebooks, ML models (Logistic Regression / SVM / embeddings)  
- **Deployment**: Streamlit app  

---

## Reports  
- Project methodology  
- Exploratory Data Analysis (EDA)  
- Model evaluation metrics (accuracy, F1, confusion matrix)  
- Policy/HR recommendations  

---

## License  
This project is licensed under the MIT License – see [LICENSE](LICENSE) for details.  

---

## Contributors  

- Kavya Adimoolam
https://github.com/Adi-k27
-  Vasanth Gnana Seelan
https://github.com/vasanthgnanaseelan

- Algonquin College Applied Research Day – Original presentation & demo  
