#!/usr/bin/python
#title          :main.py
#description    :A testing script for Guozhu Dong's CPXR algorithm
#author         :Henry Lin
#version        :0.0.1
#python_version :2.7.6
#================================================================================

import numpy as np
import pandas as pd
from sklearn.cross_validation import KFold
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

numFolds = 10
SEED = 888
np.random.seed(SEED)

def main():
    """Ross Quinlan's servo dataset. It's interesting in the way that
    it consists of only categorical variables for a regression problem.

    Full information of the dataset is provided here:
    https://archive.ics.uci.edu/ml/datasets/Servo
    """

    colnames = ["motor", "screw", "pgain", "vgain", "class"]
    dataset = pd.read_csv("data/servo.data", sep=",", names=colnames)

    # Some data preprocessing
    X = dataset.drop("class", axis=1)
    Y = dataset["class"]
    X_conv = pd.get_dummies(X, columns=colnames[:-1])
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
