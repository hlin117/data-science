#!/bin/bash

# A general script to retrieve some regression datasets from UCI
# Abalone data
echo "Downloading abalone data"
if [ -f "abalone.data" ]; then
    rm "abalone.data"
fi
wget -q http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data

# CPU data
echo "Downloading CPU data"
if [ -f "machine.data" ]; then
    rm "machine.data"
fi
wget -q http://archive.ics.uci.edu/ml/machine-learning-databases/cpu-performance/machine.data

# Servo data
echo "Downloading Servo data"
if [ -f "servo.data" ]; then
    rm "servo.data"
fi
wget -q http://archive.ics.uci.edu/ml/machine-learning-databases/servo/servo.data
