"""Import data from csv function"""

import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """
    Create a function to import CSV files into a pandas DataFrame.
    Args: a url path as a string
    Returns: a data frame
    """
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        print(f"File not found at {path}")
        df = pd.DataFrame()
    return df
