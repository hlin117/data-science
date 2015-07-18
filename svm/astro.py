#!/usr/bin/env python
#title          :astro.py
#description    :SVM benchmarks on the Astroparticle Physics dataset
#author         :Henry Lin
#version        :0.0.1
#python_version :2.7.6
#================================================================================

from __future__ import division
import pandas as pd
import numpy as np
from sklearn.datasets import load_svmlight_file
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC

SEED = 888
np.random.seed(SEED)

train_X, train_y = load_svmlight_file("data/astro.train")
test_X, test_y = load_svmlight_file("data/astro.test")

def fit_predict(clf, train_X, train_y, test_X, test_y):
    clf.fit(train_X, train_y)
    predictions = clf.predict(test_X)
    accuracy = accuracy_score(test_y, predictions)
    return accuracy

# As you could see, without any modifications, SVC scores a low accuracy
Models = [LogisticRegression, SVC, LinearSVC]
for Model in Models:
    clf = Model()
    accuracy = fit_predict(clf, train_X, train_y, test_X, test_y)
    print "Accuracy of {0}: {1}".format(Model.__name__, accuracy)

# You have to rescale data to get satisfactory results
scaler = StandardScaler()
ctrain_X = scaler.fit_transform(train_X.toarray())
ctest_X = scaler.fit_transform(test_X.toarray())

for Model in Models:
    clf = Model()
    accuracy = fit_predict(clf, ctrain_X, train_y, ctest_X, test_y)
    print "New accuracy of {0}: {1}".format(Model.__name__, accuracy)

# You could try different scaling schemes as well
scaler = MinMaxScaler(feature_range=(0, 1), copy=False)
ctrain_X = scaler.fit_transform(train_X.toarray())
ctest_X = scaler.fit_transform(test_X.toarray())

for Model in Models:
    clf = Model()
    accuracy = fit_predict(clf, ctrain_X, train_y, ctest_X, test_y)
    print "Different scaling - {0}: {1}".format(Model.__name__, accuracy)

# Ultimately, you want to try different parameters
clf = SVC(C=2.0, gamma=2.0)
accuracy = fit_predict(clf, ctrain_X, train_y, ctest_X, test_y)
print "With parameters for {0}: {1}".format(SVC.__name__, accuracy)
