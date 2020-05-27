import pandas as pd
import seaborn as sns
import os
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('/home/frozenwolfy/Desktop/Ed/PS_ML/Telemarketing/calls_2cols.csv')
df.dropna(inplace=True)
print(df.head())
row,col=df.shape

counts=dict()
for i in range(row):
  counts[df.iloc[i,1]] = counts.get(df.iloc[i,1], 0) + 1

# counts=sorted(counts.items())
print(counts)

labels = counts.keys()
sizes = counts.values()
explode = (0, 0, 0, 0, 0.2, 0.3)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("""Reason for not picking up the call
""")
plt.show()

plt.bar(counts.keys(), counts.values(), color='#FF66CC')
plt.show()
