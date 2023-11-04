# for numbers

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import random

# Function to convert age groups to random ages
def age_group_to_random_age(age_group):
    if age_group == '25-44':
        return random.randint(25, 44)
    elif age_group == '18-24':
        return random.randint(18, 24)
    elif age_group == '45-64':
        return random.randint(45, 64)
    elif age_group == '<18':
        return random.randint(12, 17)
    elif age_group == '65+':
        return random.randint(65, 80)  # Assuming 100 as the maximum age
    else:
        return None  # Handle any other cases


df = pd.read_csv('./data/arrests-data-by-new-york-police-department/NYPD_Arrests_Data__Historic_.csv')

# Apply the function to the AgeGroup column and create a new column 'Age'
df['AGE_GROUP'] = df['AGE_GROUP'].apply(age_group_to_random_age)


df=df.drop_duplicates()
df = df.dropna()
#4 million records it's a lot
df = df.sample(n=500, random_state=42)

st.sidebar.title("Filter Data on pies")



df = df.rename(columns={'ARREST_DATE':'Date', 'ARREST_KEY':'ID', 'PD_CD':'PDcode', 'PD_DESC':'PDdesc', 'KY_CD':'KYdesc', 'OFNS_DESC':'Desc', 'LAW_CODE':'CoLaw', 'LAW_CAT_CD':'Oflevel', 'ARREST_BORO':'Boro', 'ARREST_PRECINCT':'Precinct', 'JURISDICTION_CODE':'Jurisdiction', 'AGE_GROUP':'Age', 'PERP_SEX':'Sex', 'PERP_RACE':'Race'}, index={'ARREST_DATE': 'Date'})
df = df.drop(columns={'X_COORD_CD', 'Y_COORD_CD'})


df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

df['Boro'] = df['Boro'].replace({'Q': 'Queens', 'M': 'Manhattan', 'S': 'Staten Island', 'B': 'Bronx', 'K': 'Brooklyn'})
df['Sex'] = df['Sex'].replace({'M': 'Male', 'F': 'Female'})
df['Oflevel'] = df['Oflevel'].replace({'F': 'Felony', 'M': 'Misdemeanor', 'V': 'Violation'})
df['Jurisdiction'] = df['Jurisdiction'].replace({'0': 'Patrol', '1': 'Transit', '2': 'Housing'})

df['PDdesc'] = df['PDdesc'].str.capitalize()
df['Race'] = df['Race'].str.title()
df['Desc'] = df['Desc'].str.capitalize()


default_boro_filter=['Brooklyn','Bronx','Manhattan']
default_race_filter=['Black','White']
default_crime_filter=['Robbery','Dangerous weapons']
default_oflevel_filter=['Violation','Misdemeanor','Felony']
default_age_filter=['25-44','18-24','45-64','65+']
default_sex_filter=['Male','Female']

boro_filter = st.sidebar.multiselect("Select Boroughs:", df['Boro'].unique(),default_boro_filter)
race_filter = st.sidebar.multiselect("Select Races:", df['Race'].unique(),default_race_filter)

crime_filter = st.sidebar.multiselect("Select Crime", df['Desc'].unique(),default_crime_filter)
#oflevel_filter=st.sidebar.multiselect("Select Type Crime:", df['Oflevel'].unique(),default_oflevel_filter)
#age_filter=st.sidebar.multiselect('Select Age',df['Age'].unique(),default_age_filter)
sex_filter=st.sidebar.multiselect('Sex filter',df['Sex'].unique(),default_sex_filter)




# Filtering the data based on user selections
filtered_df_boro_race = df[df['Boro'].isin(boro_filter) & df['Race'].isin(race_filter)]
filtered_df_boro_crime_race=df[df['Desc'].isin(crime_filter) & df['Race'].isin(race_filter)]
filtered_df_sex_race=df[df['Sex'].isin(sex_filter) & df['Race'].isin(race_filter)]


# Create three histograms for Age, Sex, and Crime
st.title("Histograms")

# Histogram for Age
st.subheader("Age Distribution")
age_hist = px.histogram(df['Age'], x='Age', title='Age Distribution')
age_hist.update_traces(opacity=0.75)#hz
age_hist.update_traces(histnorm='probability density')#hz
st.plotly_chart(age_hist)

# Histogram for Sex
st.subheader("Sex Distribution")
sex_hist = px.histogram(df['Sex'], x='Sex', title='Sex Distribution')
st.plotly_chart(sex_hist)

# Histogram for Crime
st.subheader("Crime Distribution")
crime_hist = px.histogram(df['Oflevel'], x='Oflevel', title='Crime Distribution')
st.plotly_chart(crime_hist)


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

# Create pie chart based on filters
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
