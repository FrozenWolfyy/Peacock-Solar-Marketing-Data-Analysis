import pandas as pd
import seaborn as sns
import os
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

df=pd.read_csv('/home/frozenwolfy/Desktop/Ed/PS_ML/Peacock Solar Marketing Data Analysis/Final_project_Task 4/data/marital_status.csv')
# print(df.head())

counts=dict()
row,col=df.shape

mapping_dict={
"Marital Status":{"Single":1,"Married":2,"Relationship":2,"Undisclosed" : 0}
}
df.replace(mapping_dict,inplace=True)
print(df.head())

for i in range(row):
    if(df.iloc[i,0]!=1 and df.iloc[i,0]!=2):
        df.iloc[i,0]=0

for i in range(row):
    counts[df.iloc[i,0]] = counts.get(df.iloc[i,0], 0) + 1
print(counts)

###############################################
##################PIE-DIAGRAM##################
###############################################
#
labels = {"Married","Single","Undisclosed"}
sizes = counts.values()
explode = (0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("""Marital Status
""")
plt.show()
#
#
# ##############################################
# ###############HISTOGRAM######################
# ##############################################
#
plt.bar(counts.keys(), counts.values(), color='#FF66CC')
plt.title("""Marital Status
""")
plt.show()
