import streamlit as st
from utils.data_loader import load_cleaned_data
from utils.sentiment import apply_sentiment_label

# Harassment & Discrimination Plots
from utils.harassment_analysis import (
    plot_q57, plot_q58, plot_q59, plot_q60, plot_q61, plot_q63
)
from utils.discrimination_analysis import plot_q65, plot_q66

# ------------------------------
# Config
# ------------------------------
st.set_page_config(page_title="Sentiment & Discrimination Dashboard", layout="wide")

DATA_PATH = r"E:\BISI\Project\sentimentalanalysis\data\cleaned\Cleaned Subset 3.csv"

@st.cache_data
def get_data():
    df = load_cleaned_data(DATA_PATH)
    df = apply_sentiment_label(df)
    return df

df = get_data()

# ------------------------------
# UI
# ------------------------------
st.title("Government Survey: Sentiment, Harassment & Discrimination Insights")

# Sidebar topic menu
topic = st.sidebar.radio(
    "Select Analysis Topic",
    ["Harassment Analysis", "Discrimination Analysis"]
)

# Sidebar gender filter
gender = st.sidebar.selectbox(
    "Select Gender",
    ["Women", "Men"]
)

# ------------------------------
# Harassment Analysis Q57–Q63
# ------------------------------
if topic == "Harassment Analysis":
    st.subheader(f"Harassment Reporting ({gender})")
    st.plotly_chart(plot_q57(df, gender=gender), use_container_width=True)

    st.subheader(f"Sources of Harassment ({gender})")
    st.plotly_chart(plot_q58(df, gender=gender), use_container_width=True)

    st.subheader(f"Nature of Harassment ({gender})")
    st.plotly_chart(plot_q59(df, gender=gender), use_container_width=True)

    st.subheader(f"Actions Taken ({gender})")
    st.plotly_chart(plot_q60(df, gender=gender), use_container_width=True)

    st.subheader(f"Reasons for Not Filing Grievance ({gender})")
    st.plotly_chart(plot_q61(df, gender=gender), use_container_width=True)

    st.subheader(f"Perception of Prevention Efforts ({gender})")
    st.plotly_chart(plot_q63(df, gender=gender), use_container_width=True)

# ------------------------------
# Discrimination Analysis Q65–Q66
# ------------------------------
elif topic == "Discrimination Analysis":
    st.subheader(f"Discrimination Sources ({gender})")
    st.plotly_chart(plot_q65(df, gender=gender), use_container_width=True)

    st.subheader(f"Discrimination Types ({gender})")
    st.plotly_chart(plot_q66(df, gender=gender), use_container_width=True)

# ------------------------------
# Optional Raw Data View
# ------------------------------
with st.expander("Show Raw Data Preview"):
    st.dataframe(df.head(100))
