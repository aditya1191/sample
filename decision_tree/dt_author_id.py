#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.tree import DecisionTreeClassifier
import numpy

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

print(len(features_train[0]))


#########################################################
### your code goes here ###
#################### decision tree classifier ######################

# clf = DecisionTreeClassifier(random_state=0)
clf_40 = DecisionTreeClassifier(random_state=0, min_samples_split=40)

t0 = time()
# clf.fit(features_train, labels_train)
clf_40.fit(features_train, labels_train)
print('training time: ', round(time() - t0, 3), 's')

t0=time()
pred_40 = clf_40.predict(features_test)
# # chris = [prediction for prediction in pred_40 if prediction == 1]
# # print(pred_40[10])
# # print(len(chris))
print('prediction time: ', round(time() - t0, 3), 's')

unique, counts = numpy.unique(pred_40, return_counts=True)
print({'chris':v for (k,v) in dict(zip(unique, counts)).items() if k == 0 })

from sklearn.metrics import accuracy_score

print(accuracy_score(y_pred=pred_40, y_true=labels_test))
# #########################################################


