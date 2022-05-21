#!/usr/bin/env python3
#
# Author: Jonathan Heard
# Work on learning how to import and manipulate CVS data in Pyton.
#   The starting point for this learning is https://www.educba.com/python-import-csv/.
#
#
# Import all required items.
#

import pandas

df = pandas.read_csv('Celestial_Objects.csv')

for i in range(2):

    print(i, df.iloc[i, 0])
    print(df.iloc[i, 1] * 10)

    n = df.iloc[i, 0] + df.iloc[i, 1] * 10

    print(f"New n = {n}")
