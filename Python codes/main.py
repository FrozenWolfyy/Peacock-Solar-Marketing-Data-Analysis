import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('/home/frozenwolfy/Desktop/Ed/PS_ML/test2.csv')


row,col=df.shape



mapping_dict={
"Age ":{
"15-25" : 0,
"25-35" : 1,
"35-60" : 2,
"60+" : 3,
},
"Gender":{
"Male":0,
"Female":1,
"Nan": -1
},
"Marital Status" :{
"Single" : 0,
"Married" : 1
},

}

# print(df.iloc[100,2])

# for i in range(row):
#     print(type(df.iloc[i,1]))

df=df.replace(mapping_dict)

for j in range(1,2):
    for i in range(row):
        if(df.iloc[j,2]!=0 and df.iloc[i,2]!=1):
            df.iloc[j,2]=None

df.dropna(inplace=True)
# print(df.head())
