import pandas as pd
import plotly.express as px

def get_bycond(gender):
    gender = gender.lower()
    if gender == "men":
        return "Q117 = 1"
    return "Q117 = 2"  # default to women

def plot_q57(df, gender="Women"):
    bycond = get_bycond(gender)
    df_q57 = df[(df["question"] == "Q57") & (df["bycond"] == bycond)].copy()
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
        title=f"Q57 – {gender} Reporting Harassment at Work (Past 12 Months)",
        labels={"surveyr": "Year", "harassed_pct": "% Harassed"}
    )
    fig.update_layout(hovermode="x unified", xaxis=dict(dtick=1), yaxis=dict(title="% Harassed"), width=800, height=500)
    return fig

def plot_q58(df, gender="Women"):
    bycond = get_bycond(gender)
    df_q58 = df[(df["question"].str.match(r"Q58[a-g]")) & (df["bycond"] == bycond)].copy()
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
        title=f"Q58 – Harassment Sources Reported by {gender} (Trend)",
        labels={"surveyr": "Year", "harassed_pct": "% Harassed"}
    )
    fig.update_layout(hovermode="x unified", xaxis=dict(dtick=1), yaxis_title="% Harassed", width=1000, height=600,
                      legend_title_text="Source", legend=dict(orientation="h", y=-0.3))
    return fig

def plot_q59(df, gender="Women"):
    bycond = get_bycond(gender)
    df_q59 = df[df["question"].str.match(r"Q59[a-m]") & (df["bycond"] == bycond)].copy()
    df_q59["harassment_type"] = df_q59["title_e"].str.extract(
        r"Question 59[a-m]\. Please indicate the nature of the harassment you experienced\. (.+)", expand=False)
    df_q59["harassed_pct"] = pd.to_numeric(df_q59["answer1"], errors="coerce")
    df_q59["anscount"] = pd.to_numeric(df_q59["anscount"], errors="coerce")
    df_q59["label"] = (
        "Year: " + df_q59["surveyr"].astype(str) +
        "<br>Type: " + df_q59["harassment_type"] +
        "<br>% Harassed: " + df_q59["harassed_pct"].astype(str) +
        "<br>ANSCOUNT: " + df_q59["anscount"].astype(str)
    )
    fig = px.line(df_q59, x="surveyr", y="harassed_pct", color="harassment_type",
                  hover_name="label", markers=True,
                  title=f"Q59 – Nature of Harassment Experienced by {gender} (2018–2022)",
                  labels={"surveyr": "Year", "harassed_pct": "% Harassed"})
    fig.update_layout(width=1100, height=650, legend_title="Harassment Type", hovermode="x unified", xaxis=dict(dtick=1))
    return fig

def plot_q60(df, gender="Women"):
    bycond = get_bycond(gender)
    df_q60 = df[
        df["question"].str.match(r"Q60[a-i]", case=False, na=False) &
        (df["bycond"].str.strip() == bycond)
    ].copy()

    # Updated label map based on title_e
    label_map = {
        "I discussed the matter with my supervisor or a senior manager": "Spoke to manager",
        "I discussed the matter with the person(s) from whom I experienced the harassment": "Spoke to harasser",
        "I contacted a human resources advisor in my department or agency": "Contacted HR",
        "I contacted my union representative": "Union rep",
        "I used an informal conflict resolution process": "Conflict resolution",
        "I filed a grievance or formal complaint": "Filed complaint",
        "I resolved the matter informally on my own": "Resolved informally",
        "Other": "Other",
        "I took no action": "Took no action"
    }

    # Properly extract action text
    df_q60["action_taken"] = df_q60["title_e"].str.extract(
        r"Question 60[a-i]\. What action\(s\) did you take to address the harassment you experienced\? (.+)", expand=False
    ).str.strip().str.rstrip(".")  # Clean trailing punctuation

    # Apply label map
    df_q60["action_taken_short"] = df_q60["action_taken"].map(label_map).fillna(df_q60["action_taken"])

    # Metrics
    df_q60["pct_action"] = pd.to_numeric(df_q60["answer1"], errors="coerce")
    df_q60["anscount"] = pd.to_numeric(df_q60["anscount"], errors="coerce")
    df_q60["surveyr"] = pd.to_numeric(df_q60["surveyr"], errors="coerce")

    # Hover tooltip
    df_q60["hover_label"] = (
        "Year: " + df_q60["surveyr"].astype(str) +
        "<br>Action: " + df_q60["action_taken"] +
        "<br>% Took Action: " + df_q60["pct_action"].astype(str) +
        "<br>Responses: " + df_q60["anscount"].astype(str)
    )

    # Plot
    fig = px.line(
        df_q60,
        x="surveyr",
        y="pct_action",
        color="action_taken_short",
        markers=True,
        hover_name="hover_label",
        title=f"Q60 – Actions {gender} Took to Address Harassment (2018–2022)",
        labels={"surveyr": "Year", "pct_action": "% Who Took This Action"}
    )

    fig.update_layout(
        width=1150,
        height=650,
        legend_title="Action Taken",
        hovermode="x unified",
        xaxis=dict(dtick=1)
    )

    return fig


def plot_q61(df, gender="Women"):
    bycond = get_bycond(gender)
    df_q61 = df[df["question"].str.match(r"Q61[a-p]", case=False, na=False) & (df["bycond"].str.strip() == bycond)].copy()
    label_map = {
        "The issue was resolved": "Resolved",
        "The behaviour stopped": "Behaviour stopped",
        "I changed jobs": "Changed jobs",
        "Management intervened": "Mgmt intervened",
        "I did not think the incident was serious enough": "Not serious",
        "The individual apologized": "Apologized",
        "The individual left or changed jobs": "Indiv left",
        "I did not know what to do, where to go or whom to ask": "Didn’t know",
        "I was too distraught": "Too distraught",
        "I had concerns about the formal complaint process (e.g., confidentiality, how long it would take)": "Concerned",
        "I was advised against filing a complaint": "Advised against",
        "I was afraid of reprisal (e.g., having limited career advancement, being labelled a troublemaker)": "Fear of reprisal",
        "I did not believe it would make a difference": "No impact",
        "The time limit to file a grievance or a formal complaint had passed": "Time limit",
        "Other": "Other"
    }
    df_q61["reason_not_filed"] = df_q61["title_e"].str.extract(r"harassment you experienced\? (.+)", expand=False).str.strip(" .")
    df_q61["reason_not_filed_short"] = df_q61["reason_not_filed"].map(label_map).fillna(df_q61["reason_not_filed"])
    df_q61["pct_reason"] = pd.to_numeric(df_q61["answer1"], errors="coerce")
    df_q61["anscount"] = pd.to_numeric(df_q61["anscount"], errors="coerce")
    df_q61["surveyr"] = pd.to_numeric(df_q61["surveyr"], errors="coerce")
    df_q61["hover_label"] = (
        "Year: " + df_q61["surveyr"].astype(str) +
        "<br>Reason: " + df_q61["reason_not_filed"] +
        "<br>%: " + df_q61["pct_reason"].astype(str) +
        "<br>Responses: " + df_q61["anscount"].astype(str)
    )
    fig = px.line(df_q61, x="surveyr", y="pct_reason", color="reason_not_filed_short", markers=True,
                  hover_name="hover_label", title=f"Q61 – Why {gender} Didn't File a Harassment Grievance (2018–2022)",
                  labels={"surveyr": "Year", "pct_reason": "% Gave This Reason"})
    fig.update_layout(width=1150, height=650, legend_title="Reason", hovermode="x unified", xaxis=dict(dtick=1))
    return fig

def plot_q63(df, gender="Women"):
    bycond = get_bycond(gender)
    df_q63 = df[(df["question"].str.match(r"Q63")) & (df["bycond"] == bycond)].copy()
    df_q63["surveyr"] = pd.to_numeric(df_q63["surveyr"], errors="coerce")
    df_q63["most_positive"] = pd.to_numeric(df_q63["most_positive_or_least_negative"], errors="coerce")
    df_q63["most_negative"] = pd.to_numeric(df_q63["most_negative_or_least_positive"], errors="coerce")
    df_q63["anscount"] = pd.to_numeric(df_q63["anscount"], errors="coerce")

    df_q63_melted = df_q63.melt(
        id_vars=["surveyr", "anscount"],
        value_vars=["most_positive", "most_negative"],
        var_name="sentiment_type",
        value_name="percentage"
    )

    df_q63_melted["sentiment_type"] = df_q63_melted["sentiment_type"].map({
        "most_positive": "Most Positive / Least Negative",
        "most_negative": "Most Negative / Least Positive"
    })

    df_q63_melted["hover"] = (
        "Year: " + df_q63_melted["surveyr"].astype(str) +
        "<br>Sentiment: " + df_q63_melted["sentiment_type"] +
        "<br>% Respondents: " + df_q63_melted["percentage"].astype(str) +
        "<br>Total Responses: " + df_q63_melted["anscount"].astype(str)
    )

    fig = px.line(df_q63_melted, x="surveyr", y="percentage", color="sentiment_type",
                  hover_name="hover", markers=True,
                  title=f"Q63 – Perception of Harassment Prevention Efforts ({gender}, 2018–2022)",
                  labels={"surveyr": "Year", "percentage": "% Respondents"})
    fig.update_layout(width=1100, height=600, legend_title="Sentiment Category", hovermode="x unified",
                      xaxis=dict(dtick=1, title="Year"), yaxis=dict(title="% Respondents", range=[0, 100]))
    return fig
