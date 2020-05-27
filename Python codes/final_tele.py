import pandas as pd
import seaborn as sns
import os
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('/home/frozenwolfy/Desktop/Ed/PS_ML/final_data.csv')

# df.dropna(inplace=True)
# print(df.head())

row,col=df.shape

values={"Picked the phone" : 0,"Lead Interested or Not" :0}
df.fillna(value=values,inplace=True)

mapping_dict={
"Lead Validation" :{"Valid Contact":1,"Invalid Contact" :0 },
"Picked the phone" :{"Yes":1,"No":0,"Call Later":2},
"City" : {"Kota" :1, "Jaipur" : 2,"Indore":3,"Other":0},
"Lead Interested or Not":{"Yes":1,"No":0}
}

df.replace(mapping_dict,inplace=True)
# print(df.head())

print(df.head())
df.to_csv('processed_data.csv', encoding='utf-8')
df.to_csv('processed_data_without_index.csv', encoding='utf-8',index=False)
