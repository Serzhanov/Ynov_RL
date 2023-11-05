# Crime Data Analysis and Visualization

This project is a Streamlit web application for analyzing and visualizing crime data. It includes data preprocessing, interactive filtering, histograms, pie charts, and a geographical map with a heatmap layer.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Data Analysis Summary](#data-analysis-summary)
- [Developer Guide](#developer-guide)
- [License](#license)

## Overview

This project provides a web-based interface for analyzing and visualizing crime data from the New York Police Department. It allows users to filter data based on various criteria, view histograms of age, sex, and crime data, and generate pie charts based on user-selected filters. Additionally, the project includes a Folium map with a heatmap layer to visualize the geographical distribution of crime data.

## Features

- Data preprocessing and filtering.
- Interactive filtering with a user-friendly web interface.
- Histograms for age, sex, and crime data.
- Pie charts to visualize crime data based on filters.
- Geographical map with a heatmap layer to show crime distribution.

## Requirements

- Python 3.x
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Serzhanov/Ynov_RL.git
   cd Ynov_RL

2. Install all requirements & fetch data:
   pip install -r requirements.txt

3. Download data:
   -cd data
   -python get_data.py
    - {"username":"nurbekserzhanov","key":"22428bfc29fca4dd29a805d7cb7ab091"}

## Usage:
    #get back to main repository cd ..

    streamlit run main.py

Open a web browser and navigate to the URL provided by Streamlit (typically http://localhost:8501).
Use the web interface to interact with the crime data. You can filter the data and generate pie charts,also view histograms.
Explore the geographical distribution of crime data on the map with the heatmap layer.


## Data Analysis Summary

Below are the main conclusions extracted from the analysis of the crime data:

1. **Age Distribution:** The age distribution of individuals involved in crimes is broad, with a significant number of cases falling in the 18-44 age group.

2. **Sex Distribution:** The data shows that crimes are more commonly committed by males compared to females.

3. **Crime Distribution:** The distribution of crime types indicates that dangerous drugs and assault offense crimes are among the most prevalent.

4. **Borough Analysis:** Among the boroughs in New York, Brooklyn, Bronx, and Manhattan have the highest number of reported arrests.

5. **Race Distribution:** The racial distribution of individuals involved in crimes is diverse, with Black and White Hispanic individuals being the most prominent groups.

6. **Crime Type Distribution:** Crimes are categorized into felonies, misdemeanors, and violations, with misdemeanors being the most common type.

7. **Geographical Distribution:** The geographical map with a heatmap layer reveals the hotspots of criminal activities

These insights provide a valuable overview of crime patterns in New York, helping to identify key areas and demographics of interest for law enforcement and policymakers.


## Developer Guide

This section provides an overview of the code's architecture and guidelines for making modifications or extensions.

### Code Structure

The code is organized into several modules, classes, and functions to maintain a clear and structured design. Here's an overview of the main components:

- `main.py`: Entry point for the Streamlit application.
- `data_processing.py`: Contains functions for data processing and filtering logic.
- `data_visualization.py`: Contains functions for creating histograms, pie charts, and the Folium map.
- `folium_map.py`: Defines the Folium map component for displaying the geographical heatmap.
- `utils.py`: Includes utility functions, such as converting age groups to random ages.
- `get_data.py` : Download data via Kaggle API.

### Making Modifications

If you intend to make modifications to this code, follow these guidelines:

1. **Code Readability**: Ensure that your code is well-structured, documented, and adheres to best practices of the Python language.

2. **Data Processing**: If you want to modify the data processing logic, you can find it in `data_processing.py`.

3. **Data Visualization**: For changes related to data visualization, such as histograms, pie charts, and the Folium map, refer to `data_visualization.py` and `folium_map.py`.

4. **Extending Functionality**: To add new features or extend the application's functionality, create new functions or modules as needed and ensure they are properly integrated with the existing code.

### Dependencies

Before making changes, ensure that you have the necessary dependencies installed, including Streamlit, Plotly Express, Pandas, and Folium. You can install them using `pip`:

```bash
python -m pip install -r requirements.txt
```

## License
This project is licensed under the MIT License.
