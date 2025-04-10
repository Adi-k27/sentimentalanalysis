import streamlit as st
st.set_page_config(page_title="Sentiment Analysis Dashboard", layout="wide")

from utils.data_loader import load_cleaned_data
from utils.sentiment import apply_sentiment_label
from utils.q57_to_q63_analysis import plot_q57, plot_q58
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
    ["Q57–Q58: Harassment by Women", "Q65–Q66: Discrimination by Men"]
)

if menu == "Q57–Q58: Harassment by Women":
    st.header("Q57 – Harassment Reporting (Women)")
    st.plotly_chart(plot_q57(df), use_container_width=True)

    st.header("Q58 – Harassment Sources (Women)")
    st.plotly_chart(plot_q58(df), use_container_width=True)

elif menu == "Q65–Q66: Discrimination by Men":
    st.header("Q65 – Discrimination Sources (Men)")
    st.plotly_chart(plot_q65(df), use_container_width=True)

    st.header("Q66 – Discrimination Types (Men)")
    st.plotly_chart(plot_q66(df), use_container_width=True)

# Optional: Show raw data
with st.expander("🔍 Show Raw Data"):
    st.dataframe(df.head(100))
