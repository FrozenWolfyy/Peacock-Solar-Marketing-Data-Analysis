import pandas as pd
import numpy as np

df=pd.read_csv('/home/frozenwolfy/Desktop/Ed/PS_ML/Peacock Solar Marketing Data Analysis/Final_project_Task 4/data/cities_states.csv')
df2=pd.read_csv('/home/frozenwolfy/states.csv')
# print(df2.head())

row2,col2=df.shape
row,col=df.shape
for i in range(row):
    s=str(df.iloc[i,0])
    s=s.lower()
    for j in range(row2):
        p=str(df2.iloc[j,0])
        p=p.lower()
        if (s==p):
            df[i,0]=df2.iloc[j,1]
            break

print(df.head())
df.to_csv('cities_states_no_indexed.csv', encoding='utf-8',index=False)


# s=df.iloc[1,0]
# print(s.lower())

# df.iloc[0,0]=s.lower()
# print(df.iloc[0,0])
# s=""
# for i in range(row):
#     s=df.iloc[i,0]

    # df.iloc[i,0]=df.iloc[i,0].lower()
