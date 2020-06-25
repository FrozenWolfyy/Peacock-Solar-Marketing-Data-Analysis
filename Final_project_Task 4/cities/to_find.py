import pandas as pd
import numpy as np

df=pd.read_csv('PS_cities_2.csv')
row1,col1=df.shape

df2=pd.read_csv('git_cities.csv')
row2,col2=df2.shape

for i in range(row1):
    s=str(df.iloc[i,0]).lower()
    # print(s)
    for j in range(row2):
        # print(df2.iloc[j,0].lower())
        if(s==str(df2.iloc[j,0]).lower()):
            df.iloc[i,0]=df2.iloc[j,1]
            print(i)
            break
df.to_csv('cities_final.csv', encoding='utf-8',index=False)
