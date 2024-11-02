# Spotify Top 50 Tracks of 2020 Analysis

## Table of Contents

- [Project Overview](#project-overview)
- [Key Findings](#key-findings)
- [Installation](#installation)
  - [Clone the Repository](#clone-the-repository)
  - [Create and Activate Virtual Environment](#create-and-activate-virtual-environment)
  - [Install Dependencies](#install-dependencies)
  - [Run Jupyter Notebook](#run-jupyter-notebook)
- [Analysis Components](#analysis-components)
- [Development](#development)
  - [Clone and Setup Virtual Environment](#clone-and-setup-virtual-environment)
  - [Install Development Dependencies](#install-development-dependencies)
  - [Run Tests](#run-tests)
- [License](#license)

## Project Overview

This project analyzes the Spotify Top 50 Tracks of 2020 dataset to derive insights into popular tracks, artists, genres, and various audio features. The analysis includes exploratory data analysis to understand music trends and success patterns.

## Key Findings

- Total observations: `50`
- Total features: `16`
- Most popular artists: **Dua Lipa**, **Travis Scott**, **Billie Eilish**
- Most represented genre: **Pop** (`28%`)
- Longest track: **SICKO MODE** (`5:13`)
- Strong correlation between loudness and energy: `0.792`

## Installation

### Clone the Repository

```bash
git clone https://github.com/vytautas-bunevicius/spotify-top-50-2020-analysis.git
cd spotify-top-50-2020-analysis
```

### Create and Activate Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -e .
```

### Run Jupyter Notebook

```bash
jupyter notebook
```

## Analysis Components

The Jupyter Notebook explores:

- Artist and album diversity
- Genre distribution
- Audio characteristics (danceability, loudness, energy)
- Feature correlations
- Track duration patterns
- Production trends

## Development

### Clone and Setup Virtual Environment

Clone the repository and set up the virtual environment as shown in the [Installation](#installation) section.

### Install Development Dependencies

```bash
pip install -e ".[dev]"
```

### Run Tests

```bash
pytest
```

## License

This project is licensed under the Unlicense - see the [LICENSE](LICENSE) file for details
