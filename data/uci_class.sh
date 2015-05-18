#!/bin/bash

# The classification problem: https://archive.ics.uci.edu/ml/datasets/Mushroom
echo "Downloading mushroom data"
if [ -f "mushroom.data" ]; then
    rm "mushroom.data"
fi
wget -q https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data
mv agaricus-lepiota.data mushroom.data

echo "Downloading breast cancer data"
if [ -f "breast.data" ]; then
    rm "breast.data"
fi
wget -q http://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data
mv breast-cancer-wisconsin.data breast.data
sed -i.bak "s/?/0/g" breast.data
rm breast.data.bak
echo "NOTE: Preprocessed the heart data by replacing the '?' with '0'"

echo "Downloading liver disorder data"
if [ -f "liver.data" ]; then
    rm "liver.data"
fi
wget -q https://archive.ics.uci.edu/ml/machine-learning-databases/liver-disorders/bupa.data
mv bupa.data liver.data

echo "Downloading sonar data"
if [ -f "sonar.data" ]; then
    rm "sonar.data"
fi
wget -q https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data
mv sonar.all-data sonar.data

echo "Downloading pima data"
if [ -f "pima.data" ]; then
    rm "pima.data"
fi
wget -q https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data
mv pima-indians-diabetes.data pima.data

# source: https://archive.ics.uci.edu/ml/datasets/Horse+Colic
echo "Downloading horse data"
if [ -f "horse.data" ]; then
    rm "horse.data"
fi
wget -q https://archive.ics.uci.edu/ml/machine-learning-databases/horse-colic/horse-colic.data
mv horse-colic.data horse.data

# source: https://archive.ics.uci.edu/ml/datasets/Statlog+%28Australian+Credit+Approval%29
echo "Downloading statlog (australian) data"
if [ -f "australian.data" ]; then
    rm "australian.data"
fi
wget -q https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/australian/australian.dat
mv australian.dat australian.data
# lymph: https://archive.ics.uci.edu/ml/datasets/Lymphography
# heart disease (cleave): https://archive.ics.uci.edu/ml/datasets/Heart+Disease
