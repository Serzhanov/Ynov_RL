import streamlit as st
import plotly.express as px
import folium_map

# Function to get multiselect filters from the sidebar
def get_multiselects_filters(df):
    default_boro_filter = ['Brooklyn', 'Bronx', 'Manhattan']
    default_race_filter = ['Black', 'White']
    default_crime_filter = ['Robbery', 'Dangerous weapons']
    default_sex_filter = ['Male', 'Female']

    boro_filter = st.sidebar.multiselect("Select Boroughs:", df['Boro'].unique(), default_boro_filter)
    race_filter = st.sidebar.multiselect("Select Races:", df['Race'].unique(), default_race_filter)
    crime_filter = st.sidebar.multiselect("Select Crime", df['Desc'].unique(), default_crime_filter)
    sex_filter = st.sidebar.multiselect('Sex filter', df['Sex'].unique(), default_sex_filter)

    # Filtering the data based on user selections
    filtered_df_boro_race = df[df['Boro'].isin(boro_filter) & df['Race'].isin(race_filter)]
    filtered_df_boro_crime_race = df[df['Desc'].isin(crime_filter) & df['Race'].isin(race_filter)]
    filtered_df_sex_race = df[df['Sex'].isin(sex_filter) & df['Race'].isin(race_filter)]

    return filtered_df_boro_race, filtered_df_boro_crime_race, filtered_df_sex_race

# Data Visualization Functions
def create_histogram(df):
    # Create and return histogram plots

    # Create three histograms for Age, Sex, and Crime
    st.title("Histograms")

    # Histogram for Age
    st.subheader("Age Distribution")
    age_hist = px.histogram(df['Age'], x='Age', title='Age Distribution')
    st.plotly_chart(age_hist)

    # Histogram for Sex
    st.subheader("Sex Distribution")
    sex_hist = px.histogram(df['Sex'], x='Sex', title='Sex Distribution')
    st.plotly_chart(sex_hist)

    # Histogram for Crime
    st.subheader("Crime Distribution")
    crime_counts = df['Desc'].value_counts()
    sorted_counts = crime_counts.sort_values(ascending=True)
    crime_bar = px.bar(x=sorted_counts.values, y=sorted_counts.index, title='Crime Distribution', labels={'x': 'Counts', 'y': 'Crime Type'})
    st.plotly_chart(crime_bar)

    # Histogram for Boro
    st.subheader("Boro Distribution")
    boro_hist = px.histogram(df['Boro'], x='Boro', title='Boro Distribution')
    st.plotly_chart(boro_hist)

    # Histogram for Race
    st.subheader("Race Distribution")
    race_hist = px.histogram(df['Race'], x='Race', title='Race Distribution')
    st.plotly_chart(race_hist)

    # Histogram for Crime type
    st.subheader("Crime type Distribution")
    crime_type_hist = px.histogram(df['Oflevel'], x='Oflevel', title='Crime type Distribution')
    st.plotly_chart(crime_type_hist)

# Data Visualization Functions (continued)
def create_pie_chart(filtered_df_boro_race, filtered_df_boro_crime_race, filtered_df_sex_race):
    # Create pie charts based on filters
    st.title("Pie Charts")

    # Pie chart based on Borough and Race filters
    st.subheader("Arrests by Borough (Filtered)")
    filtered_boro_counts = filtered_df_boro_race['Boro'].value_counts().reset_index()
    filtered_boro_counts.columns = ['Borough', 'Count']
    fig_filtered_boro = px.pie(filtered_boro_counts, names='Borough', values='Count', title='Arrests by Borough (Filtered)')
    st.plotly_chart(fig_filtered_boro)

    # Pie chart based on Crime and Race filters
    st.subheader("Arrests by Crime (Filtered)")
    filtered_crime_counts = filtered_df_boro_crime_race['Desc'].value_counts().reset_index()
    filtered_crime_counts.columns = ['Desc', 'Count']
    fig_filtered_crime = px.pie(filtered_crime_counts, names='Desc', values='Count', title='Arrests by Crime (Filtered)')
    st.plotly_chart(fig_filtered_crime)

    # Pie chart based on Age, Sex, and Race filters
    st.subheader("Arrests by Age, Sex, and Race (Filtered)")
    filtered_sex_race_counts = filtered_df_sex_race.groupby(['Sex', 'Race']).size().reset_index(name='Count')
    fig_filtered_sex_race = px.pie(filtered_sex_race_counts, names='Race', values='Count', title='Arrests by Sex and Race (Filtered)')
    st.plotly_chart(fig_filtered_sex_race)

# Folium Map Functions (continued)
def create_folium_map(df):
    # Create and return a Folium map in the Streamlit app

    st.title("Folium Map")
    st.write("Map with HeatMap")

    df['Latitude'] = df['Latitude'].astype(float)
    df['Longitude'] = df['Longitude'].astype(float)

    # Create and display the Folium map
    map_component = folium_map.folium_map(df)
    st.components.v1.html(map_component._repr_html_(), width=700, height=500, scrolling=True)