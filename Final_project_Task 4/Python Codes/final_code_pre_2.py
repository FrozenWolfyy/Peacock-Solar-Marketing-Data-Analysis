import pandas as pd
import numpy as np

df=pd.read_csv('/home/frozenwolfy/Desktop/Ed/PS_ML/Peacock Solar Marketing Data Analysis/Final_project_Task 4/Python Codes/Model_with_this_data.csv')

# print(df.head())

row,col=df.shape
print(row)
# for i in range(col):
#     print(df.iloc[0,i])

counts=dict()
for i in range(row):
    if(len(str(df.iloc[i,8]))>1 or df.iloc[i,8]=='.'):
        df.iloc[i,8]='0'
    counts[df.iloc[i,8]] = counts.get(df.iloc[i,8], 0) + 1
print(counts)

# # print(type(df.iloc[0,0]))
#
# # for i in range(row):
# #     if(len(str(df.iloc[i,13]))>2 or df.iloc[i,13]=="Na"):
# #         df.iloc[i,13]=None
# # df.dropna(inplace=True)
# # row,col=df.shape
# # print(row)
#
# mapping_dict={"Home Loan ":
# {"Yes":1,"No":0},
# "How much do you expect to at least save on your average electricity bill by installing a solar panel system?" :
# {"10% - 20%" : 0, "21% - 30%" : 1, "31% - 40%" : 2, "41% - 50%": 3,">50%":4}
#  }
#
# # print(df.iloc[138,8])

# df.replace(mapping_dict,inplace=True)
df.to_csv('Model_with_this_data.csv', encoding='utf-8',index=False)
