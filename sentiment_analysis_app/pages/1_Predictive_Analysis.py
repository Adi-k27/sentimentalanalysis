import glob
import os
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from utils.data_loader import load_cleaned_data
from utils.sentiment import apply_sentiment_label
from joblib import load

# Load pre-trained model-related objects
models = load("models/sentiment_models.joblib")        # dict of sentiment models
scaler = load("models/scaler.joblib")                  # fitted scaler
label_encoders = load("models/label_encoders.joblib")  # dict of encoders
features = load("models/features.joblib")              # list of input features
categorical_cols = load("models/categorical_cols.joblib")  # categorical features
targets = [
    "MOST_POSITIVE_OR_LEAST_NEGATIVE",
    "NEUTRAL_OR_MIDDLE_CATEGORY",
    "MOST_NEGATIVE_OR_LEAST_POSITIVE"
] #output targets


# Page Title
st.title("Sentiment Forecasting (Predictive ML)")

# Dropdown options
departments = ["Health Canada", "Transport Canada", "Statistics Canada"]
questions = {
    "Q80": "Question 80. I would describe my workplace as being psychologically healthy."
}
indicators = {
    "Workplace well-being": ["A psychologically healthy workplace", "Work-life balance"]
}
years = [2018, 2019, 2020, 2021, 2022]

# Input Form
with st.form("predict_form"):
    bycond = st.selectbox("BYCOND", ["Q117 = 1", "Q117 = 2"])
    descrip_E = st.selectbox("Department", departments)
    surveyr = st.selectbox("Base Year (SURVEYR)", years)
    question = st.selectbox("Question Code", list(questions.keys()))
    title_e = questions[question]
    indicator = st.selectbox("Indicator", list(indicators.keys()))
    subindicator = st.selectbox("Subindicator", indicators[indicator])
    submit = st.form_submit_button("Predict Future Sentiment")

# Run prediction when form is submitted

if submit:
    st.success("Form submitted. Running prediction...")

    base_year = int(surveyr)

    # Function to predict sentiment
    def predict_sentiment(new_data):
        new_data_df = pd.DataFrame([new_data], columns=features)

        for col in categorical_cols:
            if new_data_df[col][0] not in label_encoders[col].classes_:
                label_encoders[col].classes_ = np.append(label_encoders[col].classes_, new_data_df[col][0])
            try:
                new_data_df[col] = label_encoders[col].transform(new_data_df[col].astype(str))
            except ValueError:
                new_data_df[col] = -1

        new_data_df["SURVEYR"] = pd.to_numeric(new_data_df["SURVEYR"], errors="coerce")
        new_data_df.fillna(0, inplace=True)
        new_data_df = scaler.transform(new_data_df)

        predictions = {sent: models[sent].predict(new_data_df)[0] for sent in targets}
        return predictions

    # Predict for current and next 2 years
    results = []
    for year in [base_year, base_year + 1, base_year + 2, base_year +3, base_year + 4]:
        input_data = {
            "BYCOND": bycond,
            "descrip_E": descrip_E,
            "SURVEYR": year,
            "QUESTION": question,
            "TITLE_E": title_e,
            "INDICATORENG": indicator,
            "SUBINDICATORENG": subindicator,
        }
        prediction = predict_sentiment(input_data)
        prediction["Year"] = year
        results.append(prediction)

    # Convert to DataFrame
    pred_df = pd.DataFrame(results)
    pred_df.rename(columns={
    "MOST_POSITIVE_OR_LEAST_NEGATIVE": "Positive",
    "NEUTRAL_OR_MIDDLE_CATEGORY": "Neutral",
    "MOST_NEGATIVE_OR_LEAST_POSITIVE": "Negative"
}, inplace=True)


    # Display table
    st.subheader("Predicted Sentiment Scores")
    st.dataframe(pred_df.set_index("Year"))

    # Display line plot
    pred_df_melted = pred_df.melt(id_vars="Year", var_name="Sentiment", value_name="Score")
    fig = px.line(pred_df_melted, x="Year", y="Score", color="Sentiment", markers=True,
                  title="Predicted Sentiment Scores (Next 3 Years)")
    st.plotly_chart(fig, use_container_width=True)

    # Debug info (optional)
    st.write("Loaded Models:", list(models.keys()))
    st.write("Features:", features)
    st.write("Categorical Columns:", categorical_cols)
    st.write("Label Encoders:", list(label_encoders.keys()))
    st.write("Input Data:", input_data)