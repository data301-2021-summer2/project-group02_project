import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def get_real_state(state):
    list_drop=[3,7,14,43]
    if state>52:
        state=state-1
    if state>43:
        state=state-1
    if state>14:
        state=state-1
    if state>7:
        state=state-1
    if state>3:
        state=state-1
    return state

def clean_data(path):
    df=(pd.read_csv(path,index_col=0)
        .dropna(axis=0)
        .loc[lambda x:x["Year"]>=1985]
        .loc[lambda x:x["Year"]<=2015]
        .drop(["County","countyBirths"],axis=1)
    )
    return df

def load_and_process(path):

    # read csv file
    df=clean_data(path)

    # create a dict to save the births of states in every month
    state_births_month={}
    # format: {state:{year:{month:births}}}

    # the index is from 1 to length of data
    for i in df.index:
        # get data for a row
        year=df["Year"][i]
        month=df["Month"][i]
        state=df["State"][i]
        births=df["stateBirths"][i]


        if year>=2003:
            state=get_real_state(state)

        if state not in state_births_month.keys():
            state_births_month[state]={}
        if year not in state_births_month[state].keys():
            state_births_month[state][year]={}
        if month not in state_births_month[state][year].keys():
            state_births_month[state][year][month]=births

    # get a dict of state data at years
    state_births_year={}
    for state in state_births_month:
        state_births_year[state]={}
        for year in state_births_month[state]:
            state_births_year[state][year]=0
            for month in state_births_month[state][year]:
                state_births_year[state][year]=state_births_year[state][year]+state_births_month[state][year][month]

        state_births_year[state]=pd.Series(state_births_year[state])

    df_state_year=pd.DataFrame(state_births_year)

    state_births={"births":[]}
    for state in state_births_year:
        state_births["births"].append(0)
        for year_births in state_births_year[state]:
            state_births["births"][-1]=state_births["births"][-1]+year_births

    # format：
    df_state_births=pd.DataFrame(state_births,index=df_state_year.columns)

    return state_births_month, df_state_year, df_state_births