#!/usr/bin/python
#title          :iris.py
#description    :A testing script for Guozhu Dong's CPXR algorithm on abalone data
#author         :Henry Lin
#version        :0.0.1
#python_version :2.7.6
#================================================================================

from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import numpy as np
import pandas as pd
from sklearn.cross_validation import KFold
from sklearn.metrics import accuracy_score

SEED = 888
np.random.seed(SEED)
numFolds = 10

def main():

    # Note that the iris dataset is available in sklearn by default.
    # This data is also conveniently preprocessed.
    iris = datasets.load_iris()
    X = iris["data"]
    Y = iris["target"]

    kf = KFold(len(X), numFolds, shuffle=True)

    # These are "Class objects". For each Class, find the AUC through
    # 10 fold cross validation.
    Models = [LogisticRegression, RandomForestClassifier, SVC]
    for Model in Models:
        total = 0
        for train_indices, test_indices in kf:

            # Get the dataset; this is the way to access values in a pandas DataFrame
            train_X = X[train_indices, :]; train_Y = Y[train_indices]
            test_X = X[test_indices, :]; test_Y = Y[test_indices]

            # Train the model, and evaluate it
            reg = Model()
            reg.fit(train_X, train_Y)
            predictions = reg.predict(test_X)
            total += accuracy_score(test_Y, predictions)
        accuracy = total / numFolds
        print "Accuracy score of {0}: {1}".format(Model.__name__, accuracy)

if __name__ == "__main__":
    main()
