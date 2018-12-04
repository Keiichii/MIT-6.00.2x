# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 15:08:10 2018

@author: usov
"""

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    N = len(L)
    if N == 0:
        return float('NaN')
    Sum = 0
    for x in L:
        Sum += len(x)
    mean = Sum / N
    tot = 0.0
    for x in L:
        tot += (len(x)-mean)**2
    std = (tot / N)**0.5
    return std

L = ['a', 'z', 'p']
L = ['apples', 'oranges', 'kiwis', 'pineapples']
L = [10, 4, 12, 15, 20, 5]
print(stdDevOfLengths(L))