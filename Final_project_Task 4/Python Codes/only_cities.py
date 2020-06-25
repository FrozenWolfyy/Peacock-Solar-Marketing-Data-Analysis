import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('/home/frozenwolfy/Desktop/Ed/PS_ML/Peacock Solar Marketing Data Analysis/Final_project_Task 4/Python Codes/Model_with_this_data.csv')

print(df.iloc[0,13])

counts=dict()

row,col=df.shape

for i in range(row):
    counts[df.iloc[i,13]] = counts.get(df.iloc[i,13], 0) + 1

print(counts)

###############################################
##################PIE-DIAGRAM##################
###############################################

labels = counts.keys()
sizes = counts.values()
# explode = (0.1, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("""Different States
""")
plt.show()


##############################################
###############HISTOGRAM######################
##############################################

plt.bar(counts.keys(), counts.values(), color='#FF66CC')
plt.title("""Different States
""")
plt.show()
