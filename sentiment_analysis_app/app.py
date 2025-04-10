import streamlit as st
st.set_page_config(page_title="Sentiment Analysis Dashboard", layout="wide")

from utils.data_loader import load_cleaned_data
from utils.sentiment import apply_sentiment_label
from utils.q57_to_q63_analysis import (plot_q57, plot_q58, plot_q59, plot_q60, plot_q61, plot_q63)

from utils.q65_q66_analysis import plot_q65, plot_q66

# Load data
DATA_PATH = r"E:\BISI\Project\sentimentalanalysis\data\cleaned\Cleaned Subset 3.csv"

@st.cache_data
def get_data():
    df = load_cleaned_data(DATA_PATH)
    df = apply_sentiment_label(df)
    return df

df = get_data()

st.title("Government Survey Sentiment & Discrimination Dashboard")


menu = st.sidebar.radio(
    "Choose Analysis",
    ["Harassment faced by Women", "Discrimination faced by Men"]
)

if menu == "Harassment faced by Women":
    st.header("Q57 – Harassment Reporting (Women)")
    st.plotly_chart(plot_q57(df), use_container_width=True)

    st.header("Q58 – Harassment Sources (Women)")
    st.plotly_chart(plot_q58(df), use_container_width=True)

    st.header("Q59 – Nature of Harassment Experienced (Women)")
    st.plotly_chart(plot_q59(df), use_container_width=True)

    st.header("Q60 – Actions Taken by Women")
    st.plotly_chart(plot_q60(df), use_container_width=True)

    st.header("Q61 – Why Women Didn't File a Grievance")
    st.plotly_chart(plot_q61(df), use_container_width=True)

    st.header("Q63 – Perception of Harassment Prevention (Women)")
    st.plotly_chart(plot_q63(df), use_container_width=True)

elif menu == "Discrimination faced by Men":
    st.header("Q65 – Discrimination Sources (Men)")
    st.plotly_chart(plot_q65(df), use_container_width=True)

    st.header("Q66 – Discrimination Types (Men)")
    st.plotly_chart(plot_q66(df), use_container_width=True)

# Optional: Show raw data
with st.expander("Show Raw Data"):
    st.dataframe(df.head(100))
