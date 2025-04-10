import pandas as pd
import plotly.express as px

def plot_q65(df):
    df_q65 = df[
        (df["question"].str.match(r"Q65[a-g]")) & (df["bycond"] == "Q117 = 1")
    ].copy()
    df_q65["Discrimination Source"] = df_q65["title_e"].str.extract(
        r"Question 65[a-g]\. From whom did you experience discrimination on the job\? (.+)"
    )
    df_q65["Discrimination %"] = pd.to_numeric(df_q65["answer1"], errors="coerce")
    df_q65["anscount"] = pd.to_numeric(df_q65["anscount"], errors="coerce")
    df_q65["Label"] = (
        "Year: " + df_q65["surveyr"].astype(str) +
        "<br>Source: " + df_q65["Discrimination Source"] +
        "<br>%: " + df_q65["Discrimination %"].astype(str) +
        "<br>anscount: " + df_q65["anscount"].astype(str)
    )
    fig = px.line(
        df_q65,
        x="surveyr",
        y="Discrimination %",
        color="Discrimination Source",
        markers=True,
        hover_name="Label",
        title="Q65a–g: Discrimination Sources Reported Over Time (Men)",
        labels={"surveyr": "Survey Year", "Discrimination %": "Reported Discrimination (%)"}
    )
    fig.update_layout(
        hovermode="x unified",
        xaxis=dict(dtick=1),
        yaxis=dict(title="Reported Discrimination (%)"),
        width=1000,
        height=600,
        legend_title_text="Source",
        legend=dict(orientation="h", y=-0.3)
    )
    return fig

def plot_q66(df):
    df_q66 = df[
        (df["question"].str.startswith("Q66")) & (df["bycond"] == "Q117 = 1")
    ].copy()
    df_q66["Discrimination Full"] = df_q66["title_e"].str.extract(
        r"Question 66[a-n]\. Please indicate the type of discrimination you experienced\. (.+)"
    )
    label_map = {
        "Race": "Race",
        "National or ethnic origin": "Ethnicity",
        "Colour": "Colour",
        "Religion": "Religion",
        "Age": "Age",
        "Sex": "Sex",
        "Sexual orientation": "Sexual Orient.",
        "Gender identity or expression (including gender diverse identities or expressions such as transgender, two-spirit, or non-binary)": "Gender Identity",
        "Marital status": "Marital Status",
        "Family status": "Family Status",
        "Genetic characteristics (including a requirement to undergo a genetic test, or disclose the results of a genetic test)": "Genetic Traits",
        "Disability": "Disability",
        "Pardoned conviction or suspended record": "Pardoned Conviction",
        "Other": "Other"
    }
    df_q66["Discrimination Type"] = df_q66["Discrimination Full"].map(label_map)
    df_q66["Discrimination %"] = pd.to_numeric(df_q66["answer1"], errors="coerce")
    df_q66["anscount"] = pd.to_numeric(df_q66["anscount"], errors="coerce")
    df_q66["Label"] = (
        "Year: " + df_q66["surveyr"].astype(str) +
        "<br>Type: " + df_q66["Discrimination Type"] +
        "<br>%: " + df_q66["Discrimination %"].astype(str) +
        "<br>anscount: " + df_q66["anscount"].astype(str)
    )
    fig = px.line(
        df_q66,
        x="surveyr",
        y="Discrimination %",
        color="Discrimination Type",
        markers=True,
        hover_name="Label",
        title="Reported Discrimination by Type Over Time (Men)",
        labels={"surveyr": "Year", "Discrimination %": "Reported Discrimination (%)"}
    )
    fig.update_layout(
        hovermode="x unified",
        xaxis=dict(dtick=1),
        yaxis=dict(title="Reported Discrimination (%)"),
        legend_title_text="Type",
        width=1000,
        height=600,
        legend=dict(orientation="h", y=-0.3)
    )
    return fig
