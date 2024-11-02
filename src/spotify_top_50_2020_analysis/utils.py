from pathlib import Path
from typing import Dict
import numpy as np
import pandas as pd


def find_project_root() -> Path:
    """
    Find the project root directory by looking for pyproject.toml.

    Returns:
        Path: Path to project root directory
    """
    current = Path.cwd()
    for parent in [current, *current.parents]:
        if (parent / "pyproject.toml").exists():
            return parent
    raise FileNotFoundError(
        "Could not find project root directory (no pyproject.toml found)"
    )


def load_spotify_data(file_name: str = "spotifytoptracks.csv") -> pd.DataFrame:
    """
    Load Spotify tracks dataset from the data directory.

    Args:
        file_name (str): Name of the CSV file to load

    Returns:
        pd.DataFrame: Loaded Spotify tracks data

    Raises:
        FileNotFoundError: If the CSV file cannot be found in the data directory
    """
    try:
        project_root = find_project_root()
        file_path = project_root / "data" / file_name

        if not file_path.is_file():
            raise FileNotFoundError(
                f"Could not find {file_name} in the data directory. "
                f"Please ensure the file exists at {file_path}"
            )

        df = pd.read_csv(file_path)
        print(f"Successfully loaded data from: {file_path}")
        return df

    except Exception as e:
        print(f"Error loading data: {e}")
        print(f"Current working directory: {Path.cwd()}")
        print(
            f"Attempted file path: {file_path if 'file_path' in locals() else 'Not determined'}"
        )
        raise

def detect_outliers(
    df: pd.DataFrame, method: str = 'iqr', threshold: float = 1.5
) -> Dict[str, pd.Series]:
    """Detects outliers in numerical columns of a DataFrame using specified method.

    Args:
        df: Input DataFrame containing the data.
        method: Method to use for outlier detection. Either 'iqr' or 'zscore'.
            Defaults to 'iqr'.
        threshold: Threshold for outlier detection.
            For IQR method: Typically 1.5 (mild outliers) or 3.0 (extreme outliers)
            For Z-score method: Typically 3.0 (3 standard deviations)
            Defaults to 1.5.

    Returns:
        Dictionary with column names as keys and Series of outliers as values.
        For columns with no outliers, an empty Series is returned.

    Raises:
        ValueError: If an invalid method is specified.

    Examples:
        >>> df = pd.DataFrame({'A': [1, 2, 3, 100, 4, 5]})
        >>> outliers = detect_outliers(df)
        >>> print(outliers['A'])
        3    100
        Name: A, dtype: int64
    """
    numeric_df = df.select_dtypes(include=[np.number])

    if not numeric_df.columns.any():
        return {}

    outliers = {}

    if method.lower() == 'iqr':
        q1 = numeric_df.quantile(0.25)
        q3 = numeric_df.quantile(0.75)
        iqr = q3 - q1

        lower_bound = q1 - threshold * iqr
        upper_bound = q3 + threshold * iqr

        for column in numeric_df.columns:
            mask = (
                (numeric_df[column] < lower_bound[column]) |
                (numeric_df[column] > upper_bound[column])
            )
            outliers[column] = numeric_df[column][mask]

    elif method.lower() == 'zscore':
        z_scores = (numeric_df - numeric_df.mean()) / numeric_df.std()

        for column in numeric_df.columns:
            mask = abs(z_scores[column]) > threshold
            outliers[column] = numeric_df[column][mask]

    else:
        raise ValueError(f"Invalid method '{method}'. Use 'iqr' or 'zscore'.")

    for column in df.columns:
        if column not in outliers:
            outliers[column] = pd.Series(dtype=df[column].dtype)

    return outliers


def print_outliers(outliers: Dict[str, pd.Series]) -> None:
    """Prints outliers in a formatted way.

    Args:
        outliers: Dictionary of outliers as returned by detect_outliers().
    """
    for column, values in outliers.items():
        if values.empty:
            print(f"\nNo outliers in {column}")
        else:
            print(f"\nOutliers in {column}:")
            print(values)
