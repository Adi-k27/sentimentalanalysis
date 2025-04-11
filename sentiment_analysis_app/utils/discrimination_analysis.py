import pandas as pd
import plotly.express as px


def get_bycond(gender):
    """Return the bycond filter string based on gender input."""
    gender = gender.lower()
    if gender == "women":
        return "Q117 = 2"
    return "Q117 = 1"  # default to men


def plot_q65(df, gender="Men", return_data=False):
    bycond = get_bycond(gender)

    df_q65 = df[
        (df["question"].str.match(r"Q65[a-g]")) & (df["bycond"] == bycond)
    ].copy()

    # Extract raw source from title
    df_q65["Discrimination Raw"] = df_q65["title_e"].str.extract(
        r"Question 65[a-g]\. From whom did you experience discrimination on the job\? (.+)"
    )

    # Apply cleaned label map
    label_map_q65 = {
        "Co-workers": "Co-workers",
        "Individuals with authority over me": "Supervisors",
        "Individuals working for me": "Subordinates",
        "Individuals for whom I have a custodial responsibility (e.g., inmates, offenders, patients, detainees)": "Custodial Responsibility",
        "Individuals from other departments or agencies": "Other Departments/Agencies",
        "Members of the public (individuals or organizations)": "Public/Organizations",
        "Other": "Other"
    }
    df_q65["Discrimination Source"] = df_q65["Discrimination Raw"].map(label_map_q65)
    df_q65["Discrimination Source"].fillna("Unknown", inplace=True)

    # Convert relevant fields to numeric
    df_q65["Discrimination %"] = pd.to_numeric(df_q65["answer1"], errors="coerce")
    df_q65["anscount"] = pd.to_numeric(df_q65["anscount"], errors="coerce")
    df_q65.sort_values("surveyr", inplace=True)

    # Hover label formatting
    df_q65["Label"] = (
        "Year: " + df_q65["surveyr"].astype(str) +
        "<br>Source: " + df_q65["Discrimination Source"] +
        "<br>%: " + df_q65["Discrimination %"].astype(str) +
        "<br>anscount: " + df_q65["anscount"].astype(str)
    )

    # Plot
    fig = px.line(
        df_q65,
        x="surveyr",
        y="Discrimination %",
        color="Discrimination Source",
        markers=True,
        hover_name="Label",
        title=f"Q65a–g: Discrimination Sources Reported Over Time ({gender})",
        labels={"surveyr": "Survey Year", "Discrimination %": "Reported Discrimination (%)"}
    )

    fig.update_layout(
        hovermode="x unified",
        xaxis=dict(dtick=1, rangeslider=dict(visible=True)),
        yaxis=dict(title="Reported Discrimination (%)"),
        width=1000,
        height=600,
        legend_title_text="Source",
        legend=dict(orientation="v", x=1.02, y=1),
        margin=dict(l=80, r=200, t=80, b=80)
    )

    return (fig, df_q65) if return_data else fig



def plot_q66(df, gender="Men", return_data=False):
    bycond = get_bycond(gender)

    df_q66 = df[
        (df["question"].str.startswith("Q66")) & (df["bycond"] == bycond)
    ].copy()

    # Extract discrimination type
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
    df_q66["Discrimination Type"].fillna("Unknown", inplace=True)

    # Convert to numeric
    df_q66["Discrimination %"] = pd.to_numeric(df_q66["answer1"], errors="coerce")
    df_q66["anscount"] = pd.to_numeric(df_q66["anscount"], errors="coerce")

    # Sort by year
    df_q66.sort_values("surveyr", inplace=True)

    # Hover labels
    df_q66["Label"] = (
        "Year: " + df_q66["surveyr"].astype(str) +
        "<br>Type: " + df_q66["Discrimination Type"] +
        "<br>%: " + df_q66["Discrimination %"].astype(str) +
        "<br>anscount: " + df_q66["anscount"].astype(str)
    )

    # Plot
    fig = px.line(
        df_q66,
        x="surveyr",
        y="Discrimination %",
        color="Discrimination Type",
        markers=True,
        hover_name="Label",
        title=f"Q66a–n: Discrimination Types Reported Over Time ({gender})",
        labels={"surveyr": "Year", "Discrimination %": "Reported Discrimination (%)"}
    )

    fig.update_layout(
        hovermode="x unified",
        xaxis=dict(dtick=1, rangeslider=dict(visible=True)),
        yaxis=dict(title="Reported Discrimination (%)"),
        width=1000,
        height=600,
        legend_title_text="Type",
        legend=dict(orientation="v", x=1.02, y=1),
        margin=dict(l=80, r=200, t=80, b=80)
    )

    return (fig, df_q66) if return_data else fig