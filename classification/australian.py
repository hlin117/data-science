#!/usr/bin/env python
#title          :australian.py
#description    :A general classification task
#author         :Henry Lin
#version        :0.0.1
#python_version :2.7.6
#================================================================================

from __future__ import division
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split, KFold
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC, LinearSVC

SEED = 888
np.random.seed(SEED)
numFolds = 10

def main():

    dataset = pd.read_csv("data/australian.data", header=None, sep=" ")
    X = dataset.drop(14, axis=1)
    Y = dataset[14]
    conv_X = pd.get_dummies(X, columns=[0, 3, 4, 5, 7, 8, 10, 11])

    # These are "Class objects". For each Class, find the AUC through
    # 10 fold cross validation.
    Models = [LogisticRegression, RandomForestClassifier, SVC, LinearSVC]
    params = [{}, {}, {}, {}]
    for Model, params in zip(Models, params):
        total = 0
        kf = KFold(len(X), numFolds, shuffle=True, random_state=SEED)
        for train_indices, test_indices in kf:

            # Get the dataset; this is the way to access values in a pandas DataFrame
            train_X = conv_X.ix[train_indices, :]; train_Y = Y[train_indices]
            test_X = conv_X.ix[test_indices, :]; test_Y = Y[test_indices]

            # Train the model, and evaluate it
            reg = Model(**params)
            reg.fit(train_X, train_Y)
            predictions = reg.predict(test_X)
            fpr, tpr, _ = roc_curve(test_Y, predictions)
            total += auc(fpr, tpr)
        accuracy = total / numFolds
        print "AUC of {0}: {1}".format(Model.__name__, accuracy)

if __name__ == "__main__":
    main()
