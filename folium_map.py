import pandas as pd
import folium
from folium.plugins import HeatMap

# Function to create a Folium map with a HeatMap layer
def folium_map(dataframe):

    dataframe = dataframe[pd.notnull(dataframe['Latitude'])]
    dataframe = dataframe[pd.notnull(dataframe['Longitude'])]
    # Create a Folium map centered at the mean latitude and longitude of the filtered data
    m = folium.Map(location=[40.7221, -73.9198], zoom_start=11)
    # Create heat data as a list of latitude and longitude pairs
    heat_data = [[row['Latitude'], row['Longitude']] for index, row in dataframe.iterrows()]
    # Add a HeatMap layer to the map
    HeatMap(heat_data).add_to(m)
    return m