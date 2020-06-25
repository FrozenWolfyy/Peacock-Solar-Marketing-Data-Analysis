import pandas as pd

df=pd.read_csv('/home/frozenwolfy/Desktop/Ed/PS_ML/Peacock Solar Marketing Data Analysis/Final_project_Task 4/Python Codes/Model_with_this_data.csv')

# print(df.iloc[0,13])

counts=dict()
row,col=df.shape

for i in range(row):
    counts[df.iloc[i,13]] = counts.get(df.iloc[i,13], 0) + 1

print(counts)
