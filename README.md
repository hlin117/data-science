# Data Science
Some general machine learning exercises one can run to get used to python's
scientific computing libraries.

## Getting the most from this project

First off, read this README!

In any given script, there are a lot of moving components flying around that
are important to understanding the modeling and evaluation process.
If you're new to modeling, here are some basic questions you could ask yourself:

* What is classification? What is regression?
* What is the UCI machine learning repository? Why is it used as a benchmark
in many papers that introduce machine learning models?
* What is the difference between python `pandas`, `numpy`, and `scikit-learn`?
* How are the models in each of the scripts different from each other?
* What is k-fold cross validation?
* The iris dataset uses `accuracy_score` to evaluate its models for
classification. What is the difference between evaluating a model using AUC
and an accuracy score? Why can't we use AUC to evaluate the models trained
in the iris dataset?

## Missing bits and pieces

You could help contribute to this project! See below for contribution rules.
Some popular tasks that are currently missing are:

- Multitask Classification (The iris dataset is the only multi-class problem)
- Clustering (It's hard to get ground truth data sets)
- Text mining (Again, hard to obtain ground truth)
- Computer Vision (Not my area of specialty)

This repository primarily fetches from the UCI machine learning repository.
Please `cd data` to see the fetching scripts, and the URLs for each address.

## Installing the required packages
I put everything into a requirements file. Just do

```
pip install -r requirements.txt
```

and let the magic of pip take over. If you need to install these packages on
a machine you don't have `sudo` access to, throw in the `--user` argument.

# Contributing to this project
I'd love it if people contributed to this repository. But here are some ground
rules, just to make sure the coding style is consistent.

1. Use 4 spaced indents, no tabs.
2. Try to keep lines within 80 characters, even in the README.md.
(PEP 8 says 79, I'm a bit more flexible.) If you use vim 7.4, I'd recommend
using the `set colorcolumn=80` setting.
3. Do not commit data sets. Create simple fetching scripts like I do.
4. Avoid small changes to commits, if possible. (Yes, I'm guilty of doing this
too.) Perform a `git rebase` whenever you need to squash commits together.
