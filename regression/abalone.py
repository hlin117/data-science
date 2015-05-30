#!/usr/bin/python
#title          :abalone.py
#description    :A testing script for Guozhu Dong's CPXR algorithm on abalone data
#author         :Henry Lin
#version        :0.0.1
#python_version :2.7.6
#================================================================================

from __future__ import division
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
import numpy as np
import pandas as pd
from sklearn.cross_validation import KFold
from sklearn.metrics import mean_squared_error

SEED = 888
np.random.seed(SEED)
numFolds = 10

def main():
    """The prediction task is to predict the number of rings on an abalone,
    a kind of shellfish.

    Full information of the dataset is provided here:
    https://archive.ics.uci.edu/ml/datasets/Abalone
    """

    colnames = ["sex", "length", "diameter", "height", "whole_weight", \
            "shucked_weight", "viscera_weight", "shell_weight", "rings"]
    dataset = pd.read_csv("data/abalone.data", names=colnames)

    # Some data preprocessing
    X = dataset.drop("rings", axis=1)
    Y = dataset["rings"]
    X_conv = pd.get_dummies(X, columns=["sex"])
    kf = KFold(len(X), numFolds, shuffle=True)

    Models = [LinearRegression, RandomForestRegressor, SVR]
    for Model in Models:
        total = 0
        for train_indices, test_indices in kf:
            X_train = X_conv.ix[train_indices, :]; Y_train = Y[train_indices]
            X_test = X_conv.ix[test_indices, :]; Y_test = Y[test_indices]

            # Testing out on the linear regression
            reg = Model()
            reg.fit(X_train, Y_train)

            predictions = reg.predict(X_test)
            mse = mean_squared_error(Y_test, predictions)
            total += mse
        mse = total / numFolds
        print "Average mse of {0}: {1}".format(Model.__name__, mse)

if __name__ == "__main__":
    main()
