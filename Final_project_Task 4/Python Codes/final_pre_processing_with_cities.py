import pandas as pd
import seaborn as sns
import os
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

df=pd.read_csv('/home/frozenwolfy/Desktop/Ed/PS_ML/Peacock Solar Marketing Data Analysis/Final_project_Task 4/Python Codes/before_pre_processing_with_cities_1.csv')
df2=pd.read_csv('/home/frozenwolfy/Desktop/Ed/PS_ML/Peacock Solar Marketing Data Analysis/Final_project_Task 4/cities/git_cities.csv')
# print(df.head())
# df.dropna(inplace=True)
# df.to_csv('before_pre_processing_with_cities_1.csv', encoding='utf-8',index=False)
df.dropna(inplace=True)
# print(type(df.iloc[0,13]))
row,col=df.shape

for i in range(row):
    if (df.iloc[i,6]=="Married"):
        df.iloc[i,6]=1
    elif (df.iloc[i,6]=="Single"):
        df.iloc[i,6]=2
    else:
        df.iloc[i,6]=0
    if(df.iloc[i,11]=="Private"):
        df.iloc[i,11]=1
    elif (df.iloc[i,11]=="Business"):
        df.iloc[i,11]=2
    elif (df.iloc[i,11]=="Government"):
        df.iloc[i,11]=3
    else:
        df.iloc[i,11]=0

#
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
#
#
#
df.replace(mapping_dict,inplace=True)
row2,col2=df2.shape

# print(df.iloc[0,13])

for i in range(row):
    s=str(df.iloc[i,13]).lower()
    for j in range(row2):
        p=df2.iloc[j,0].lower()
        if(s==p):
            df.iloc[i,13]=df2.iloc[j,1]
            break
    # if(type(df.iloc[i,13])==type("s")):
    #     df.iloc[i,13]=None
print(df.head())
df.to_csv('after_pre_processing_with_cities.csv', encoding='utf-8',index=False)
