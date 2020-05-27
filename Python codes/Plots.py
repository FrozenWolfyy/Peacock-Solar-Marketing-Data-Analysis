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

# print(df.iloc[10,1])
age0=0
age1=0
age2=0
age3=0

row,col=df.shape

for i in range(row):
    if df.iloc[i,0]==0:
        age0=age0+1
    elif(df.iloc[i,0]==1):
        age1+=1
    elif(df.iloc[i,0]==2):
        age2+=1
    elif(df.iloc[i,0]==3):
        age3+=1

print(age0,age1,age2,age3)


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = ' 15-25 ', ' 25-35 ', ' 35-60 ', ' 60+ '
sizes = [age0, age1, age2, age3]
explode = (0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("""Age Group Participated in the survey
""")
plt.show()
