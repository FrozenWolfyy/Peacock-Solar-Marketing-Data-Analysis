import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('/home/frozenwolfy/Desktop/Ed/PS_ML/how much are you aware.csv')

row,col=df.shape

df.dropna(inplace=True)

count1=0
count2=0
count3=0
count4=0
count5=0


row,col=df.shape

for i in range(row):
    if df.iloc[i,0]==1:
        count1=count1+1
    elif(df.iloc[i,0]==2):
        count2+=1
    elif(df.iloc[i,0]==3):
        count3+=1
    elif(df.iloc[i,0]==4):
        count4+=1
    elif(df.iloc[i,0]==5):
        count5+=1

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Not at all','Slightly', 'Moderately', 'Very','Extremely'
sizes = [count1, count2, count3, count4, count5]
explode = (0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("""Knowledge on Solar Power
""")
plt.show()
