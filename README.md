# Spotify Top 50 Tracks of 2020 Analysis

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
    - [Using uv (Recommended)](#using-uv-recommended)
    - [Using pip (Alternative)](#using-pip-alternative)
- [Data Analysis](#data-analysis)
    - [Exploratory Analysis](#exploratory-analysis)
- [Findings and Insights](#findings-and-insights)
- [Business Value & Applications](#business-value--applications)
- [License](#license)

## Overview

This project analyzes the Spotify Top 50 Tracks of 2020 dataset to derive
insights into popular tracks, artists, genres, and various audio features. The
analysis leverages a Jupyter Notebook to perform interactive exploratory data
analysis and understand music trends and success patterns.

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

3. **Install Dependencies and Set Up Virtual Environment:**

   ```bash
   uv sync
   ```

4. **Activate the Virtual Environment:**

   ```bash
   source .venv/bin/activate  # On Unix/macOS
   # or
   .venv\Scripts\activate     # On Windows
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

## Business Value & Applications

### For Artists & Producers

- **What Works: Rhythmic, Energetic Tracks**: 60% of Top 50 songs have high
  danceability (above 0.7). If you're producing Hip-Hop or Dance/Electronic, aim
  for similar energy levels. Example: "The Box" (0.896 danceability) and "Tusa"
  (0.803) outperformed slower tracks.

- **The Loudness-Energy Balance**: Louder songs tend to feel more energetic. You
  can succeed either way: produce loud and punchy tracks like Pop rap hits
  (-3.6 dB) or quieter, introspective ones like Billie Eilish's songs
  (-10 to -14 dB). The key is matching your genre's expectations.

- **Song Length Flexibility**: Hits don't need to be short. While "Mood" is just
  2:21, "SICKO MODE" succeeds at 5:13. Plan your track length to fit your
  production style, not arbitrary streaming limits.

- **Genre Production Benchmarks**: Different genres require different
  approaches.
  Alternative/Indie tracks average 0.66 danceability and 0.58 acousticness,
  meaning they use more acoustic instruments. Dance/Electronic averages 0.76
  danceability with almost no acousticness (0.10), meaning heavy electronic
  production.

### For Labels & Artist Management

- **Build Consistent Artists**: Three artists (Dua Lipa, Travis Scott, Billie
  Eilish) each have 3 songs in the Top 50. Focus on developing artists who can
  produce multiple hits rather than chasing one-hit wonders.

- **Album Strategy**: Dua Lipa's "Future Nostalgia" placed 3 tracks in the Top
  50
  simultaneously. A well-executed album concept can drive multiple chart
  entries,
  multiplying exposure and revenue.

- **Genre Viability**: Pop dominates at 28% of the chart, but 16 different
  genres
  are represented. You don't need to chase pop trends. There's room for Hip-Hop
  (13 tracks), R&B/Soul, Alternative, and more. Pick artists where you can build
  consistent quality.

### For Streaming Platforms & Curators

- **Playlist Segmentation**: The data shows clear clusters. 30 out of 50 tracks
  are highly danceable while only one ("lovely") is introspective and quiet.
  Build separate playlists: "High Energy" for danceability 0.7+, and "Moody"
  for emotional tracks.

- **Genre Mixing Works**: The Top 50 features fusion genres like
  "Dreampop/Hip-Hop/R&B" and "Alternative/reggaeton/experimental". Hybrid
  playlists that combine unexpected genres attract listeners seeking discovery.

## License

This project is released under the [Unlicense](https://unlicense.org/). This
means you can copy, modify, publish, use, compile, sell, or distribute this
software, either in source code form or as a compiled binary, for any purpose,
commercial or non-commercial, and by any means.

See the [UNLICENSE](UNLICENSE) file for more details.
