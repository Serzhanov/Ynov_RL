import utils
import pandas as pd

# Data Processing Functions
def process_data(df):
    # Data preprocessing and filtering logic

    # Apply the function to the AgeGroup column and create a new column 'Age'
    df['AGE_GROUP'] = df['AGE_GROUP'].apply(utils.age_group_to_random_age)

    df = df.drop_duplicates()
    df = df.dropna()
    # Sample 50000 records to reduce data size
    df = df.sample(n=50000, random_state=42)

    # Rename and preprocess columns
    df = df.rename(columns={'ARREST_DATE': 'Date', 'ARREST_KEY': 'ID', 'PD_CD': 'PDcode', 'PD_DESC': 'PDdesc', 
                           'KY_CD': 'KYdesc', 'OFNS_DESC': 'Desc', 'LAW_CODE': 'CoLaw', 'LAW_CAT_CD': 'Oflevel', 
                           'ARREST_BORO': 'Boro', 'ARREST_PRECINCT': 'Precinct', 'JURISDICTION_CODE': 'Jurisdiction', 
                           'AGE_GROUP': 'Age', 'PERP_SEX': 'Sex', 'PERP_RACE': 'Race'}, 
                           index={'ARREST_DATE': 'Date'})
    df = df.drop(columns={'X_COORD_CD', 'Y_COORD_CD'})

    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
    df['Boro'] = df['Boro'].replace({'Q': 'Queens', 'M': 'Manhattan', 'S': 'Staten Island', 'B': 'Bronx', 'K': 'Brooklyn'})
    df['Sex'] = df['Sex'].replace({'M': 'Male', 'F': 'Female'})
    df['Oflevel'] = df['Oflevel'].replace({'F': 'Felony', 'M': 'Misdemeanor', 'V': 'Violation'})
    df['Jurisdiction'] = df['Jurisdiction'].replace({'0': 'Patrol', '1': 'Transit', '2': 'Housing'})
    df['PDdesc'] = df['PDdesc'].str.capitalize()
    df['Race'] = df['Race'].str.title()
    df['Desc'] = df['Desc'].str.capitalize()

    return df