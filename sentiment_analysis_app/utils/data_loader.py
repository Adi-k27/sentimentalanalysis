import pandas as pd
import os

def load_cleaned_data(file_path):
    """
    Load the cleaned dataset CSV file and convert column names to lowercase.

    Args:
        file_path (str): Full path to the CSV file.

    Returns:
        pd.DataFrame: Loaded DataFrame
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    df = pd.read_csv(file_path)
    df.columns = df.columns.str.lower()
    return df
