import pandas as pd
import seaborn as sn
import os
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('/home/frozenwolfy/Desktop/Ed/PS_ML/Peacock Solar Marketing Data Analysis/Final_project_Task 4/ML Models/Model_with_this_data_0_1.csv')
row,col=df.shape


finalised_all_features = df[['Age', 'Monthy Earnings','New Floor','Budget','Percentage of roof dedicated','Workplace','State']].values

finalised_all_classes=df['Would you like to go for solar'].values

finalised_feature_names = ['Age', 'Monthy Earnings','New Floor','Budget','Percentage of roof dedicated','Workplace','State']


###################################################
#############PRE-PROCESSING-DATA###################
###################################################
from sklearn import preprocessing

scaler = preprocessing.StandardScaler()
finalised_all_features_scaled = scaler.fit_transform(finalised_all_features)
# print(all_features_scaled)

###################################################
#############TRAIN-TEST-SPLIT-DATA#################
###################################################


from sklearn.model_selection import train_test_split
(training_inputs,testing_inputs,training_classes,testing_classes) = train_test_split(finalised_all_features_scaled, finalised_all_classes, train_size=0.95, random_state=1)

##############K NEAREST NEIGHBOURS#########
from sklearn import neighbors
from sklearn.model_selection import cross_val_score

clf = neighbors.KNeighborsClassifier(n_neighbors=10)

clf.fit(training_inputs,training_classes)
# print(clf.predict_proba(testing_inputs))

cv_scores = cross_val_score(clf,finalised_all_features_scaled,finalised_all_classes, cv=10)
# print(cv_scores.mean())
#
##for choosing the number of neighbours of the classifier try a few values for k
##find the corresponding cv_score and choose the best fit but do not overfit your data.

for n in range(1, 50):
    clf = neighbors.KNeighborsClassifier(n_neighbors=n)
    cv_scores = cross_val_score(clf, finalised_all_features_scaled, finalised_all_classes, cv=10)
    print (n, cv_scores.mean())
