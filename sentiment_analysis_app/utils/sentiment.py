import pandas as pd

def classify_sentiment(score):
    """
    Classify sentiment based on score.

    Args:
        score (float): The sentiment score (0–100 scale).

    Returns:
        str: One of 'Positive', 'Neutral', 'Negative', or 'Unknown'
    """
    if pd.isna(score):
        return "Unknown"
    elif score >= 60:
        return "Positive"
    elif score >= 30:
        return "Neutral"
    else:
        return "Negative"

def apply_sentiment_label(df, score_col="score100"):
    """
    Add a sentiment label column to the DataFrame.
    """
    df[score_col] = pd.to_numeric(df[score_col], errors="coerce")  # <-- Add this line
    df["sentiment_label"] = df[score_col].apply(classify_sentiment)
    return df
