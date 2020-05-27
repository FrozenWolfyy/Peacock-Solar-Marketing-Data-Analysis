import pandas as pd
import seaborn as sns
import os
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('/home/frozenwolfy/Desktop/Ed/PS_ML/Telemarketing/timevspickupphone.csv')
# print(df.head())
df.dropna(inplace=True)

counts=dict()
row,col=df.shape
for i in range(row):
    s=df.iloc[i,0][9:11]
    # print(s)
    df.iloc[i,0]=s
    counts[s]=counts.get(s,0)+1

mapping_dict={
"Calling Time":{
"12":12,
"13":13,
"14":14,
"15":15,
"16":16,
"17":17,
"18":18,
"19":19,
"20":20,
"21":21,
"22":22,
"23":23,
"00":0,
"01":1,
"02":2,
"03":3,
"04":4,
"05":5,
"06":6,
"07":7,
"08":8,
"09":9,
"10":10,
"11":11
}
}

print(counts)

plt.bar(counts.keys(), counts.values(), color='#FF66CC')
plt.show()
