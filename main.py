# Import necessary libraries and modules
import pandas as pd
import streamlit as st
import data_processing
import data_visualization

# Streamlit App
def main():
    # Read the dataset
    df = pd.read_csv('./data/arrests-data-by-new-york-police-department/NYPD_Arrests_Data__Historic_.csv')

    # Create the Streamlit app
    st.sidebar.title("Filter Data on pies")

    # Data Processing
    filtered_data = data_processing.process_data(df)

    # Get multiselect filters from the sidebar
    filtered_df_boro_race, filtered_df_boro_crime_race, filtered_df_sex_race = data_visualization.get_multiselects_filters(filtered_data)

    # Data Visualization
    data_visualization.create_histogram(filtered_data)
    data_visualization.create_pie_chart(filtered_df_boro_race, filtered_df_boro_crime_race, filtered_df_sex_race)

    # Folium Map
    data_visualization.create_folium_map(filtered_data)

if __name__ == '__main__':
    main()
