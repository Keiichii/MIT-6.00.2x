# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 01:59:51 2018

@author: ART
"""
import pandas as pd


q = pd.read_hdf('foo.h5','q')

for x in q.sort_values('x').values:
    print(x[0], '=', x[2])
#    break