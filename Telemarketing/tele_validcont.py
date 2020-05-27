import pandas as pd
import seaborn as sns
import os
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('/home/frozenwolfy/Desktop/Ed/PS_ML/Telemarketing/leadValidation.csv')
df.dropna
# print(df.head())

validContact=0
invalidContact=0

row,col=df.shape

###########################COUNTER#######################
counts=dict()
for i in range(row):
  counts[df.iloc[i,0]] = counts.get(df.iloc[i,0], 0) + 1

mapping_dict={
"Lead Validation":{
"Valid Contact" : 0,
"Invalid Contact" :1
}
}

df=df.replace(mapping_dict)

for i in range(row):
    if(df.iloc[i,0]==0):
        validContact+=1
    elif(df.iloc[i,0]==1):
        invalidContact+=1
    else:
        df.iloc[i,0]=None
df.dropna



labels = 'Valid Contacts','Invalid Contacts'
sizes = [validContact, invalidContact]
explode = (0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("""Percentage of Valid contacts
""")
plt.show()

# print(validContact)
# print(invalidContact)

##############################################
###############HISTOGRAM######################
##############################################
plt.bar(counts.keys(), counts.values(), color='#FFA07A')
plt.show()
