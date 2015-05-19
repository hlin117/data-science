# Data Science
Some general machine learning exercises one can run to get used to python's
scientific computing libraries.

Some popular tasks that are currently missing are:

- Regression
- Multitask Classification
- Clustering (It's hard to get ground truth data sets)
- Text mining (Again, hard to obtain ground truth)
- Computer Vision (Not my area of specialty)

This repository primarily fetches from the UCI machine learning repository.
Please `cd data` to see the fetching scripts, and the URLs for each address.

# Installing the required packages
I put everything into a requirements file. Just do

```
pip install -r requirements.txt
```

and let the magic of pip take over.

# Contributing to this project
I'd love it if people contributed to this repository. But here are some ground
rules, just to make sure the coding style is consistent.

1. Use 4 spaced indents, no tabs.
2. Always make sure your code works in the virtual environment. This means
putting `#!/usr/bin/env python` on every executable python script.
3. Try to keep lines within 80 characters, even in the README.md.
(PEP 8 says 79, I'm a bit more flexible.) If you use vim 7.4, I'd recommend
using the `set colorcolumn=80` setting.
4. Do not commit data sets. Create simple fetching scripts like I do.
5. Avoid small changes to commits, if possible. (Yes, I'm guilty of doing this
too.) Perform a `git rebase` whenever you need to squash commits together.
