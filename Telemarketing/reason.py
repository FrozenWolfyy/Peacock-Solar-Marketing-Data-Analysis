import pandas as pd
import seaborn as sns
import os
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('/home/frozenwolfy/Desktop/Ed/PS_ML/Telemarketing/Reason.csv')
# df.dropna
row,col=df.shape
print(df.head())
# counts=dict()
# for i in range(row):
#   counts[df.iloc[i,0]] = counts.get(df.iloc[i,0], 0) + 1
#
# print(counts)

# mapping_dict={
# "Picked the phone":{
# "No" : 0,
# "Yes" : 1,
# "Call Later" :2
# }
# }
#
# df=df.replace(mappin  g_dict)

# print(df.head())

##############################################
###############HISTOGRAM######################
##############################################
# plt.bar(counts.keys(), counts.values(), color='#FF66CC')
# plt.show()
#
# #################################################
# ############PIE DIAGRAM##########################
# #################################################
#
labels = counts.keys()
sizes = counts.values()
explode = (0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("""Lead Interested or Not
""")
plt.show()
