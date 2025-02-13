# Spotify Top 50 Tracks of 2020 Analysis

## Table of Contents

- [Overview](#overview)
- [Dashboard](#dashboard)
- [Installation](#installation)
  - [Using uv (Recommended)](#using-uv-recommended)
  - [Using pip (Alternative)](#using-pip-alternative)
- [Data Analysis](#data-analysis)
  - [Exploratory Analysis](#exploratory-analysis)
- [Findings and Insights](#findings-and-insights)
- [Future Improvements](#future-improvements)
- [License](#license)

## Overview

This project analyzes the Spotify Top 50 Tracks of 2020 dataset to derive insights into popular tracks, artists, genres, and various audio features. The analysis leverages a Jupyter Notebook to perform interactive exploratory data analysis and understand music trends and success patterns.

## Dashboard

Currently, there is no interactive dashboard available. Future iterations of the project may include a dashboard for real-time data visualization.

## Installation

### Using uv (Recommended)

1. **Install uv:**

   ```bash
   # On Unix/macOS
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # On Windows (PowerShell)
   irm https://astral.sh/uv/install.ps1 | iex
   ```

2. **Clone the Repository:**

   ```bash
   git clone https://github.com/vytautas-bunevicius/spotify-top-50-2020-analysis.git
   cd spotify-top-50-2020-analysis
   ```

3. **Create and Activate a Virtual Environment:**

   ```bash
   uv venv
   source .venv/bin/activate  # On Unix/macOS
   # or
   .venv\Scripts\activate     # On Windows
   ```

4. **Install Dependencies:**

   ```bash
   uv pip install -e .
   ```

5. **Launch Jupyter Notebook:**

   ```bash
   jupyter notebook
   ```

### Using pip (Alternative)

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/vytautas-bunevicius/spotify-top-50-2020-analysis.git
   cd spotify-top-50-2020-analysis
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Unix/macOS
   # or
   venv\Scripts\activate     # On Windows
   ```

3. **Install Dependencies:**

   ```bash
   pip install -e .
   ```

4. **Launch Jupyter Notebook:**

   ```bash
   jupyter notebook
   ```

## Data Analysis

### Exploratory Analysis

The Jupyter Notebook examines several aspects of the dataset, including:

- Artist and album diversity
- Genre distribution and trends
- Audio characteristics such as danceability, loudness, and energy
- Correlations between various audio features
- Track duration patterns and production trends

## Findings and Insights

- Total observations: 50
- Total features: 16
- Most popular artists: Dua Lipa, Travis Scott, Billie Eilish
- Most represented genre: Pop (28%)
- Longest track: SICKO MODE (5:13)
- Strong correlation between loudness and energy: 0.792

## Future Improvements

Planned enhancements for future versions include:

- Development of an interactive dashboard for real-time data visualization.
- Extended analysis on year-over-year trends in music analytics.
- Integration of additional datasets for enriched insights.
- Improved hypothesis testing and predictive modeling.

## License

This project is licensed under the Unlicense - see the [LICENSE](LICENSE) file for details.
