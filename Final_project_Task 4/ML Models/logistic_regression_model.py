import pandas as pd
import seaborn as sn
import os
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('/home/frozenwolfy/Desktop/Ed/PS_ML/Peacock Solar Marketing Data Analysis/Final_project_Task 4/ML Models/Model_with_this_data_0_1.csv')
row,col=df.shape
# print(df.head())

# for col in df.columns:
#     print(col)



all_features = df[['Age', 'Monthy Earnings','Home Loan ','Expected savings','Rooms','New Floor','Budget','Percentage of roof dedicated','Workplace','State']].values
# print(all_features)

all_classes=df['Would you like to go for solar'].values
# print(all_classes)

feature_names = ['Age', 'Monthy Earnings','Home Loan ','Expected savings','Rooms','New Floor','Budget','Percentage of roof dedicated','Workplace','State']
# print(feature_names)

###################################################
#############CORRELATION MATRIX###################
###################################################

corrMatrix = df.corr()
sn.heatmap(corrMatrix, annot=True)
plt.show()
# print(corrMatrix)



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
# (training_inputs,testing_inputs,training_classes,testing_classes) = train_test_split(all_features, all_classes, train_size=0.95, random_state=1)

###################################################
#############LOGISTIC-REGRESSION##################
###################################################

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

clf = LogisticRegression()
clf.fit(training_inputs,training_classes)
# cv_scores = cross_val_score(clf, all_features, all_classes, cv=10)
cv_scores = cross_val_score(clf, all_features_scaled, all_classes, cv=10)
# print(cv_scores)

###################################################
#############FEATURE-IMPORTANCE##################
###################################################

# get importance
importance = clf.coef_[0]
# summarize feature importance
for i,v in enumerate(importance):
	print('Feature: %0d, Score: %.5f' % (i,v))


# plot feature importance

plt.bar([x for x in range(len(importance))], importance)
plt.title("Feature Importance")
plt.show()

# We can see that removing feature 2, feature 3, feature 4 improves the performance of our model


################################################################
################################################################
##########FINALISING LOGISTIC REGRESSION MODEL##################
################################################################
################################################################

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
(training_inputs,testing_inputs,training_classes,testing_classes) = train_test_split(finalised_all_features_scaled, all_classes, train_size=0.95, random_state=1)
# (training_inputs,testing_inputs,training_classes,testing_classes) = train_test_split(all_features, all_classes, train_size=0.95, random_state=1)

###################################################
#############LOGISTIC-REGRESSION##################
###################################################

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

clf = LogisticRegression()
clf.fit(training_inputs,training_classes)

# print(clf.predict(testing_inputs))
# cv_scores = cross_val_score(clf, all_features, all_classes, cv=10)
cv_scores = cross_val_score(clf, finalised_all_features_scaled, all_classes, cv=10)
print(cv_scores)






###################################################
#############FEATURE-IMPORTANCE##################
###################################################

# get importance

importance = clf.coef_[0]

# summarize feature importance
for i,v in enumerate(importance):
	print('Feature: %0d, Score: %.5f' % (i,v))

# plot feature importance

plt.bar([x for x in range(len(importance))], importance)
plt.title("Feature Importance")
plt.show()

##################################################
#################For-Predicting-New-Data##########
##################################################

# 'Age', 'Monthy Earnings','New Floor','Budget','Percentage of roof dedicated','Workplace','State'
#
# predict_1=[[1,1,0,2,1,1,36]]
# print(clf.predict_proba(predict_1))
# print(cv_scores.mean())
#
# predict_1=[[1,1,2]]   #valid Contact,picked up phone,from Jaipur
# print(clf.predict_proba(predict_1))
#
# predict_1=[[1,1,3]]   #valid Contact,picked up phone,from Indore
# print(clf.predict_proba(predict_1))
