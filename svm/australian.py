#!/usr/bin/env python
#title          :australian.py
#description    :A classification task to show how to improve SVMs
#author         :Henry Lin
#version        :0.0.1
#python_version :2.7.6
#================================================================================

from __future__ import division
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import KFold
from sklearn.svm import SVC, LinearSVC

SEED = 888
np.random.seed(SEED)
numFolds = 10

dataset = pd.read_csv("data/australian.data", header=None, sep=" ")
X = dataset.drop(14, axis=1)
Y = dataset[14]

# Produces a "one hot encoding" of the data
conv_X = pd.get_dummies(X, columns=[0, 3, 4, 5, 7, 8, 10, 11])
Models = [LogisticRegression, LinearSVC, SVC]

kf = KFold(len(X), numFolds, shuffle=True)
for Model in Models:
    total = 0
    for train_indices, test_indices in kf:

        # Get the dataset; this is the way to access values in a pandas DataFrame
        train_X = conv_X.ix[train_indices, :]; train_Y = Y[train_indices]
        test_X = conv_X.ix[test_indices, :]; test_Y = Y[test_indices]

        reg = Model()
        reg.fit(train_X, train_Y)
        predictions = reg.predict(test_X)
        total += accuracy_score(test_Y, predictions)
    accuracy = total / numFolds
    print "AUC of {0}: {1}".format(Model.__name__, accuracy)

scaler = MinMaxScaler(feature_range=(-1, 1), copy=False,
                      selected=[1, 2, 6, 9, 12, 13])
conv_X = scaler.fit_transform(X)
conv_X = pd.get_dummies(pd.DataFrame(conv_X), columns=[0, 3, 4, 5, 7, 8, 10, 11])

kf = KFold(len(X), numFolds, shuffle=True)
for Model in Models:
    total = 0
    for train_indices, test_indices in kf:

        # Get the dataset; this is the way to access values in a pandas DataFrame
        train_X = conv_X.ix[train_indices, :]; train_Y = Y[train_indices]
        test_X = conv_X.ix[test_indices, :]; test_Y = Y[test_indices]

        reg = Model()
        reg.fit(train_X, train_Y)
        predictions = reg.predict(test_X)
        total += accuracy_score(test_Y, predictions)
    accuracy = total / numFolds
    print "AUC of {0}: {1}".format(Model.__name__, accuracy)

scaler = MinMaxScaler(feature_range=(0, 1), copy=False,
                      selected=[1, 2, 6, 9, 12, 13])
conv_X = scaler.fit_transform(X)
conv_X = pd.get_dummies(pd.DataFrame(conv_X), columns=[0, 3, 4, 5, 7, 8, 10, 11])

kf = KFold(len(X), numFolds, shuffle=True)
for Model in Models:
    total = 0
    for train_indices, test_indices in kf:

        # Get the dataset; this is the way to access values in a pandas DataFrame
        train_X = conv_X.ix[train_indices, :]; train_Y = Y[train_indices]
        test_X = conv_X.ix[test_indices, :]; test_Y = Y[test_indices]

        reg = Model()
        reg.fit(train_X, train_Y)
        predictions = reg.predict(test_X)
        total += accuracy_score(test_Y, predictions)
    accuracy = total / numFolds
    print "AUC of {0}: {1}".format(Model.__name__, accuracy)

