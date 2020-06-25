import pandas as pd
import seaborn as sns
import os
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

df=pd.read_csv('/home/frozenwolfy/Desktop/Ed/PS_ML/Peacock Solar Marketing Data Analysis/Final_project_Task 4/data/data_before_preprocessing.csv')
# print(df.head())

row,col=df.shape
print(row,col)
#
# for i in range(col):
#     print(df.iloc[0,i])

counts=dict()
for i in range(row):
    if (df.iloc[i,6]=="Married"):
        df.iloc[i,6]=1
    elif (df.iloc[i,6]=="Single"):
        df.iloc[i,6]=2
    else:
        df.iloc[i,6]=0
    if(df.iloc[i,10]=="Private"):
        df.iloc[i,10]=1
    elif (df.iloc[i,10]=="Business"):
        df.iloc[i,10]=2
    elif (df.iloc[i,10]=="Government"):
        df.iloc[i,10]=3
    else:
        df.iloc[i,10]=0
    counts[df.iloc[i,10]] = counts.get(df.iloc[i,10], 0) + 1

print(counts)

# print(df.iloc[0,0])
# print(df.iloc[8,1])
# print(df.iloc[8,2])
# print(df.iloc[8,3])



mapping_dict={"Age" :
{"15-25": 0,"25-35" : 1,"35-60" : 2, "60+" : 3},
"Gender" :
{"Male" : 1, "Female" :2},
"Monthy Earnings" :
{"Less than 20000": 0 ,"20000 - 70000" : 1,"70000- 1 lakh" : 2,"1 lakh +" :3},
"Home Loan"  :
{"No" : 0, "Yes" : 1},
"Expected savings upon installing" :
{"10% - 20%" : 0, "21% - 30%" : 1, "31% - 40%" : 2, "41% - 50%" : 3, ">50%" : 4},
"Rooms" :
{"1" : 0, "2" : 1, "3" : 2, "4" : 3, "5+" : 4},
"New Floor" :
{"No" : 0, "Yes" : 1},
"Would you like to go for solar" :
{
"Saving 1000+/month saving on electricity bill after spending 55000/KW" : 1,
"Avail solar electricity at 50% down payment and rest in 6 month EMI's at 0% interest":2,
"No I'd not like to buy solar" : 0,
"Saving 1000+/month saving on electricity bill after spending 45000/KW" : 3,
},
"Budget" :
{"50000- 1 Lac" : 1, "Less than 50000" : 0 ,"1 Lac - 2 Lacs" : 2,"2 Lacs +" : 3},
"Percentage of roof dedicated" :
{"<25%" : 0, "26-50%" : 1, "51-75%" : 2, ">75%" : 3},

}
df.dropna(inplace=True)
row,col=df.shape
print(row,col)
df.replace(mapping_dict,inplace=True)
print(df.head())
df.to_csv('after_pre_processing.csv', encoding='utf-8',index=False)
