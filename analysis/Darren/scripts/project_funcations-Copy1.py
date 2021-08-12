#Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt




# cleaning
def clean_data(path):
    df=(pd.read_csv(path,index_col=0)
        .rename(columns={"countyBirths": "cB"})
        .dropna(axis=0)
        .reset_index(drop=True)
        .loc[lambda x:x["Year"]>=1985]
        .loc[lambda x:x["Year"]<=2015]
        .drop(["County","countyBirths"],axis=1)
    )
    return df

# load and process
def load_and_process(path):
    df=clean_data(path)
    state_births_month={}

    for i in df.index:
        year=df["Year"][i]
        month=df["Month"][i]
        state=df["State"][i]
        births=df["stateBirths"][i]
        

        
# wrangle data
def load_USA_data(path):
    df = pd.read_csv(path, index_col=0)
    data_filter = df.loc[:, ['Year', 'countyBirths']]
    sum_data = data_filter.groupby('Year').sum()
    print(sum_data)
    return sum_data
