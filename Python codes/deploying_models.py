import pandas as pd
import seaborn as sns
import os
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('/home/frozenwolfy/Desktop/Ed/PS_ML/Python codes/processed_data_without_index.csv')
row,col=df.shape
all_features = df[['Lead Validation', 'Picked the phone','City']].values
# print(all_features)
all_classes=df['Lead Interested or Not'].values
# print(all_values)

feature_names=['Lead Validation', 'Picked the phone','City']
# print(feature_names)

###################################################
#############PRE-PROCESSING-DATA###################
###################################################
from sklearn import preprocessing

scaler = preprocessing.StandardScaler()
all_features_scaled = scaler.fit_transform(all_features)
# print(all_features_scaled)


###################################################
#############TRAIN-TEST-SPLIT-DATA#################
###################################################


from sklearn.model_selection import train_test_split
(training_inputs,testing_inputs,training_classes,testing_classes) = train_test_split(all_features_scaled, all_classes, train_size=0.95, random_state=1)



###################################################
#############LOGISTIC-REGRESSION##################
###################################################

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

clf = LogisticRegression()
clf.fit(training_inputs,training_classes)
# cv_scores = cross_val_score(clf, all_features_scaled, all_classes, cv=10)
cv_scores = cross_val_score(clf, all_features_scaled, all_classes, cv=10)


##################################################
#################For-Predicting-New-Data##########
##################################################


predict_1=[[1,1,1]]   #valid Contact,picked up phone,from kota
print(clf.predict_proba(predict_1))
# print(cv_scores.mean())

predict_1=[[1,1,2]]   #valid Contact,picked up phone,from Jaipur
print(clf.predict_proba(predict_1))

predict_1=[[1,1,3]]   #valid Contact,picked up phone,from Indore
print(clf.predict_proba(predict_1))
