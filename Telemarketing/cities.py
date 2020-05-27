import pandas as pd
import seaborn as sns
import os
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

df=pd.read_csv('/home/frozenwolfy/Desktop/Ed/PS_ML/Telemarketing/cities.csv')
df.dropna

counts = dict()
row,col=df.shape
for i in range(row):
  counts[df.iloc[i,0]] = counts.get(df.iloc[i,0], 0) + 1

# print(counts)

mapping_dict={
"City" : {
"Kota":1,
"Jaipur":2,
"Indore":3,
"Other":0
}
}

df=df.replace(mapping_dict)
# print(type(counts.keys))
print(counts.values())
print(counts.keys())


############################################
###############PIE GRAPH#####################
#############################################


# labels = counts.keys()
# sizes = counts.values()
# explode = (0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
#
# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# plt.title("""Cities from the Telemarketing data
# """)
# plt.show()


# pos = np.arange(len(counts.keys()))
# width = 1.0     # gives histogram aspect to the bar diagram
#
# ax = plt.axes()
# ax.set_xticks(pos + (width / 2))
# ax.set_xticklabels(counts.keys())
#
# plt.bar(counts.keys(),counts.values(), color='g')
# #                            ^^^^^^ what should I put here?
# plt.show()


##############################################
###############HISTOGRAM######################
##############################################
plt.bar(counts.keys(), counts.values(), color='k')
plt.show()
