# Pole data
# Source: http://mldata.org/repository/data/viewslug/regression-datasets-pol/
echo "Downloading Pole data"
if [ -f "pole.data" ]; then
    rm "pole.data"
fi

wget -q http://mldata.org/repository/data/download/csv/regression-datasets-pol/
mv index.html pole.data

# This is another dataset that contains the 5000 / 10000 data split up
# wget -q http://www.dcc.fc.up.pt/~ltorgo/Regression/pol.tgz

# Price data
# Source: http://mldata.org/repository/data/viewslug/uci-20070111-auto_price/
echo "Downloading Price data"
if [ -f "price.data" ]; then
    rm "price.data"
fi

wget -q http://mldata.org/repository/data/download/csv/uci-20070111-auto_price/
mv index.html price.data
