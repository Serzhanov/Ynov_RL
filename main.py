# Import necessary libraries and modules
import pandas as pd
import streamlit as st
import data_processing
import data_visualization
import algorithms_applicaiton

# Streamlit App
def main():
    # Read the dataset
    df = pd.read_csv('./data/arrests-data-by-new-york-police-department/NYPD_Arrests_Data__Historic_.csv')

    # Create the Streamlit app
    st.sidebar.title("Filter Data on pies")

    # Data Processing
    filtered_data = data_processing.process_data(df)
    

    # Perform one-hot encoding
    one_hot_encoded = pd.get_dummies(filtered_data['Boro'], prefix='Boro')
    

    # Get multiselect filters from the sidebar  
    filtered_df_boro_race, filtered_df_boro_crime_race, filtered_df_sex_race = data_visualization.get_multiselects_filters(filtered_data)

    # Data Visualization
    data_visualization.create_histogram(filtered_data)
    data_visualization.create_pie_chart(filtered_df_boro_race, filtered_df_boro_crime_race, filtered_df_sex_race)

    # Folium Map
    data_visualization.create_folium_map(filtered_data)

    #Multi-Plot Bandits
    '''Using Thompson sampling on district area of NY'''
    st.title('Multi-Plot Streamlit App')
    num_arms=len(one_hot_encoded.values[0])
    true_labels=one_hot_encoded.values
    timesteps,simulations=data_visualization.generate_thompson_inputs()
    regrets,names=algorithms_applicaiton.experiment(num_arms,true_labels,timesteps,simulations)
    data_visualization.multi_plot_data(regrets, names)
  

if __name__ == '__main__':
    main()
