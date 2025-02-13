"""Unit tests for the spotify_top_50_2020_analysis.utils module.

This test module provides comprehensive coverage for utility functions used in
analyzing Spotify Top 50 tracks data. It includes tests for project root
detection, data loading, outlier detection, and output formatting.

The test suite follows pytest conventions and uses fixtures and mocking to
ensure isolated testing of each component.
"""

from pathlib import Path
from unittest import mock

import pandas as pd
import pytest

from src.spotify_top_50_2020_analysis.utils import (
    detect_outliers,
    find_project_root,
    load_spotify_data,
    print_outliers,
)


@pytest.fixture
def mock_project_root(tmp_path: Path) -> Path:
    """Create a temporary project root directory with pyproject.toml.

    Args:
        tmp_path: Pytest fixture providing temporary directory path.

    Returns:
        Path: Path to temporary project root directory containing pyproject.toml.
    """
    (tmp_path / "pyproject.toml").touch()
    return tmp_path


def test_find_project_root_success(mock_project_root: Path, monkeypatch) -> None: # pylint: disable=redefined-outer-name
    """Test successful project root detection.

    Verifies that find_project_root correctly identifies a directory containing
    pyproject.toml as the project root.

    Args:
        mock_project_root: Fixture providing temporary project root.
        monkeypatch: Pytest fixture for modifying environment.
    """
    monkeypatch.chdir(mock_project_root)
    assert find_project_root() == mock_project_root


def test_find_project_root_not_found(monkeypatch, tmp_path: Path) -> None:
    """Test project root detection failure.

    Verifies that find_project_root raises FileNotFoundError when no
    pyproject.toml exists in the directory tree.

    Args:
        monkeypatch: Pytest fixture for modifying environment.
        tmp_path: Pytest fixture providing temporary directory path.
    """
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()
    monkeypatch.chdir(test_dir)

    with mock.patch("src.spotify_top_50_2020_analysis.utils.Path") as mock_path_class:
        mock_path_instance = mock.MagicMock(spec=Path)
        mock_path_instance.exists.return_value = False
        mock_file = mock.MagicMock()
        mock_file.exists.return_value = False
        mock_path_instance.__truediv__.return_value = mock_file
        mock_path_instance.parent = mock_path_instance
        mock_path_class.cwd.return_value = mock_path_instance

        with pytest.raises(FileNotFoundError):
            find_project_root()


def test_load_spotify_data_success(tmp_path: Path) -> None:
    """Test successful Spotify data loading."""
    with mock.patch(
        "src.spotify_top_50_2020_analysis.utils.find_project_root"
    ) as mock_find_root, mock.patch(
        "src.spotify_top_50_2020_analysis.utils.pd.read_csv"
    ) as mock_read_csv, mock.patch("pathlib.Path.cwd") as mock_cwd:
        project_root = tmp_path / "project"
        project_root.mkdir()
        mock_find_root.return_value = project_root
        mock_cwd.return_value = project_root

        data_dir = project_root / "data"
        data_dir.mkdir()
        csv_file = data_dir / "spotifytoptracks.csv"
        csv_file.parent.mkdir(exist_ok=True)
        csv_file.touch()

        df_expected = pd.DataFrame(
            {
                "Track": ["Song A", "Song B"],
                "Artist": ["Artist 1", "Artist 2"],
                "Duration": [210, 180],
            }
        )

        mock_read_csv.return_value = df_expected

        df = load_spotify_data()
        pd.testing.assert_frame_equal(df, df_expected)

        mock_read_csv.assert_called_once_with(csv_file)


def test_load_spotify_data_file_not_found(tmp_path: Path) -> None:
    """Test Spotify data loading with missing file.

    Verifies that load_spotify_data raises FileNotFoundError when the
    expected CSV file does not exist.

    Args:
        tmp_path: Pytest fixture providing temporary directory path.
    """
    with mock.patch(
        "src.spotify_top_50_2020_analysis.utils.find_project_root"
    ) as mock_find_root, mock.patch("pathlib.Path.exists") as mock_exists:
        project_root = tmp_path / "project"
        project_root.mkdir()
        mock_find_root.return_value = project_root

        mock_exists.return_value = False

        with pytest.raises(FileNotFoundError):
            load_spotify_data()


def test_detect_outliers_iqr() -> None:
    """Test outlier detection using IQR method.

    Verifies that detect_outliers correctly identifies outliers using the
    Interquartile Range method with default threshold.
    """
    df = pd.DataFrame({"A": [1, 2, 3, 100, 4, 5], "B": [10, 12, 14, 16, 18, 20]})
    outliers = detect_outliers(df, method="iqr", threshold=1.5)
    assert "A" in outliers
    assert outliers["A"].tolist() == [100]
    assert "B" in outliers
    assert outliers["B"].tolist() == []


def test_detect_outliers_zscore() -> None:
    """Test outlier detection using Z-score method.

    Verifies that detect_outliers correctly identifies outliers using the
    Z-score method with default threshold.
    """
    df = pd.DataFrame({"A": [1, 2, 3, 100, 4, 5], "B": [10, 12, 14, 16, 18, 20]})
    outliers = detect_outliers(df, method="zscore", threshold=2.0)
    assert "A" in outliers
    assert outliers["A"].tolist() == [100]
    assert "B" in outliers
    assert outliers["B"].tolist() == []


def test_detect_outliers_invalid_method() -> None:
    """Test outlier detection with invalid method.

    Verifies that detect_outliers raises ValueError when an invalid
    detection method is specified.
    """
    df = pd.DataFrame({"A": [1, 2, 3]})
    with pytest.raises(ValueError):
        detect_outliers(df, method="invalid", threshold=1.5)


def test_detect_outliers_no_numeric_columns() -> None:
    """Test outlier detection with non-numeric data.

    Verifies that detect_outliers returns empty dictionary when input
    DataFrame contains no numeric columns.
    """
    df = pd.DataFrame({"A": ["foo", "bar", "baz"], "B": ["apple", "banana", "cherry"]})
    outliers = detect_outliers(df)
    assert not outliers


def test_print_outliers_no_outliers(capfd) -> None:
    """Test printing of empty outliers.

    Verifies that print_outliers correctly handles and formats output when
    no outliers are present.

    Args:
        capfd: Pytest fixture for capturing stdout/stderr.
    """
    outliers = {"A": pd.Series(dtype=int)}
    print_outliers(outliers)
    captured = capfd.readouterr()
    assert "No outliers in A" in captured.out


def test_print_outliers_with_outliers(capfd) -> None:
    """Test printing of detected outliers.

    Verifies that print_outliers correctly formats and displays detected
    outliers.

    Args:
        capfd: Pytest fixture for capturing stdout/stderr.
    """
    outliers = {"A": pd.Series([100], index=[3], name="A")}
    print_outliers(outliers)
    captured = capfd.readouterr()
    assert "Outliers in A:" in captured.out
    assert "100" in captured.out


def test_load_spotify_data_exception(tmp_path: Path) -> None:
    """Test handling of data loading exceptions.

    Verifies that load_spotify_data properly handles and propagates
    exceptions that occur during data loading.

    Args:
        tmp_path: Pytest fixture providing temporary directory path.
    """
    with mock.patch(
        "src.spotify_top_50_2020_analysis.utils.find_project_root"
    ) as mock_find_root, mock.patch(
        "src.spotify_top_50_2020_analysis.utils.pd.read_csv"
    ) as mock_read_csv:
        project_root = tmp_path / "project"
        project_root.mkdir()
        mock_find_root.return_value = project_root

        data_dir = project_root / "data"
        data_dir.mkdir()
        csv_file = data_dir / "spotifytoptracks.csv"
        with open(csv_file, "w") as f:
            f.write("dummy")

        mock_read_csv.side_effect = Exception("Read error")
        with pytest.raises(Exception, match="Read error"):
            load_spotify_data()
