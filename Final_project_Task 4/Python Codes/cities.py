import pandas as pd
import seaborn as sns
import os
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

df=pd.read_csv('/home/frozenwolfy/Desktop/Ed/PS_ML/Peacock Solar Marketing Data Analysis/Final_project_Task 4/data/cities_states.csv')
# print(df.head())
df.dropna(inplace=True)
counts=dict()
row,col=df.shape

print(type(df.iloc[1,0]))
for i in range(row):
    s=df.iloc[i,0]
    b=s.lower()
    df.iloc[i,0]=b
    counts[df.iloc[i,0]] = counts.get(df.iloc[i,0], 0) + 1
print(counts)
