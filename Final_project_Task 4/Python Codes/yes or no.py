import pandas as pd
import seaborn as sns
import os
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

df=pd.read_csv('/home/frozenwolfy/Desktop/Ed/PS_ML/Peacock Solar Marketing Data Analysis/Final_project_Task 4/data/Yes or No.csv')
print(df.head())

counts=dict()
row,col=df.shape

mapping_dict={"Which one would you prefer?": 
{
"Saving 1000+/month saving on electricity bill after spending 55000/KW" : 1,
"Avail solar electricity at 50% down payment and rest in 6 month EMI's at 0% interest":2,
"No I'd not like to buy solar" : 0,
"Saving 1000+/month saving on electricity bill after spending 45000/KW" : 3,
}
}

df.replace(mapping_dict,inplace=True)

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
plt.title("""Interested in Solar or Not

""")
plt.show()


##############################################
###############HISTOGRAM######################
##############################################

plt.bar(counts.keys(), counts.values(), color='#FF66CC')
plt.title("""Interested in Solar or Not

""")
plt.show()
