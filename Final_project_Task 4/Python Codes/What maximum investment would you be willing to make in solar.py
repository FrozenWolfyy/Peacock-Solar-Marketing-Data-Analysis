import pandas as pd
import seaborn as sns
import os
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

df=pd.read_csv('/home/frozenwolfy/Desktop/Ed/PS_ML/Peacock Solar Marketing Data Analysis/Final_project_Task 4/data/What maximum investment would you be willing to make in solar.csv')
print(df.head())

counts=dict()
row,col=df.shape

for i in range(row):
    counts[df.iloc[i,0]] = counts.get(df.iloc[i,0], 0) + 1
print(counts)

#############################################
################PIE-DIAGRAM##################
#############################################

labels = counts.keys()
sizes = counts.values()
explode = (0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("""What maximum investment would you be willing to make in solar?

""")
plt.show()


##############################################
###############HISTOGRAM######################
##############################################

plt.bar(counts.keys(), counts.values(), color='#FF66CC')
plt.title("""What maximum investment would you be willing to make in solar?

""")
plt.show()
