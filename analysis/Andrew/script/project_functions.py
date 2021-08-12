import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def clean_data(path):
    data= pd.read_csv(path)
    data_clean=data.dropna(axis=0)
    data_clean = data_clean[data_clean['Year'] >= 1985]
    data_clean = data_clean[data_clean['Year']<=2015]
    return data_clean
def load_process(data,year):
    data=data[data['Year']==year]
    state_list=list(range(1,max(data['State'])+1))
    state_list
    column_names=['State','percenatge']
    df=pd.DataFrame(columns=column_names)
    df['State']=state_list
    Statebirth=[]
    df

def wrangle(old_data,new_data,new_list,newlist_name):
    for item in new_data['State']:
        new_list.append(old_data.loc[old_data['State']==item,'countyBirths'].sum())

    new_data[newlist_name]=new_list