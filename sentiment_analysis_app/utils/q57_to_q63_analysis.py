import pandas as pd
import plotly.express as px

def plot_q57(df):
    df_q57 = df[(df["question"] == "Q57") & (df["bycond"] == "Q117 = 2")].copy()
    df_q57["harassed_pct"] = pd.to_numeric(df_q57["answer1"], errors="coerce")
    df_q57["anscount"] = pd.to_numeric(df_q57["anscount"], errors="coerce")
    df_q57["label"] = (
        "Year: " + df_q57["surveyr"].astype(str) +
        "<br>% Harassed: " + df_q57["harassed_pct"].astype(str) +
        "<br>anscount: " + df_q57["anscount"].astype(str)
    )
    fig = px.line(
        df_q57,
        x="surveyr",
        y="harassed_pct",
        markers=True,
        hover_name="label",
        title="Q57 – Women Reporting Harassment at Work (Past 12 Months)",
        labels={"surveyr": "Year", "harassed_pct": "% Harassed"}
    )
    fig.update_layout(hovermode="x unified", xaxis=dict(dtick=1), yaxis=dict(title="% Harassed"), width=800, height=500)
    return fig

def plot_q58(df):
    df_q58 = df[(df["question"].str.match(r"Q58[a-g]")) & (df["bycond"] == "Q117 = 2")].copy()
    df_q58["harassment_source"] = df_q58["title_e"].str.extract(
        r"Question 58[a-g]\. From whom did you experience harassment on the job\? (.+)", expand=False
    )
    df_q58["harassed_pct"] = pd.to_numeric(df_q58["answer1"], errors="coerce")
    df_q58["anscount"] = pd.to_numeric(df_q58["anscount"], errors="coerce")
    df_q58["label"] = (
        "Year: " + df_q58["surveyr"].astype(str) +
        "<br>Source: " + df_q58["harassment_source"] +
        "<br>% Harassed: " + df_q58["harassed_pct"].astype(str) +
        "<br>ANSCOUNT: " + df_q58["anscount"].astype(str)
    )
    fig = px.line(
        df_q58,
        x="surveyr",
        y="harassed_pct",
        color="harassment_source",
        markers=True,
        hover_name="label",
        title="Q58 – Harassment Sources Reported by Women (Trend)",
        labels={"surveyr": "Year", "harassed_pct": "% Harassed"}
    )
    fig.update_layout(hovermode="x unified", xaxis=dict(dtick=1), yaxis_title="% Harassed", width=1000, height=600,
                      legend_title_text="Source", legend=dict(orientation="h", y=-0.3))
    return fig
