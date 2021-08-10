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


