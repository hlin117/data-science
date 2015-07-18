# Data from the paper "A Practical Guide to Support Vector Classification"

echo "Downloading Astroparticle Physics Data"
if [ -f "astro.train" ]; then
    rm "astro.train"
fi

if [ -f "astro.test" ]; then
    rm "astro.test"
fi

wget -q http://ntucsu.csie.ntu.edu.tw/~cjlin/papers/guide/data/test.1
mv test.1 astro.test

wget -q http://ntucsu.csie.ntu.edu.tw/~cjlin/papers/guide/data/train.1
mv train.1 astro.train
