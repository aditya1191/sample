#!/usr/bin/python3

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
import numpy

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################

from sklearn import svm

# features_train = features_train[:int(len(features_train)/100)]
# labels_train = labels_train[:int(len(labels_train)/100)]

# clf = svm.SVC()
# t0 = time()
# clf.fit(features_train, labels_train)
# print("Training Time:", round(time()-t0, 3), "s")
#################### RBF SVC ######################
rbf_svc = svm.SVC(kernel="rbf", C=10000)
t0 = time()
rbf_svc.fit(features_train, labels_train)
print("Training Time:", round(time()-t0, 3), "s")

#################### PREDICTION #####################################

t0 = time()
pred = rbf_svc.predict(features_test)

# chris = [prediction for prediction in pred if prediction == 1]
unique, counts = numpy.unique(pred, return_counts=True)

print(pred[10])
print(pred[26])
print(pred[50])

print(dict(zip(unique, counts)))

# print("Testing Time:", round(time()-t0, 3), "s")
# from sklearn.metrics import accuracy_score
# print(f"Accuracy for emails: {accuracy_score(y_pred=pred, y_true=labels_test)}")



#########################################################
'''
You'll be Provided similar code in the Quiz
But the Code provided in Quiz has an Indexing issue
The Code Below solves that issue, So use this one
'''

# features_train = features_train[:int(len(features_train)/100)]
# labels_train = labels_train[:int(len(labels_train)/100)]

#########################################################
