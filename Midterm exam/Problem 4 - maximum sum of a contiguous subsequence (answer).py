# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 00:09:17 2018

@author: ART
"""

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    #YOUR CODE HERE
    
    max_ending_here = max_so_far = L[0]
    for i in L[1:]:
        max_ending_here = max(i, max_ending_here + i)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

L = [[1], [1, -1], [10, 9, 8, -1], [-2, 6, 8, 10], [5, -7, 1], [0, -2, -5, -1, 5],
    [-3, -2, 1, -1, -5],
    [3, 4, -1, 5, -4],
    [3, 4, -8, 15, -1, 2],
    [3, 4, -8, 3, 3, 1, -7, 15, -1, 2],
    [0, -2, -7, 3, 3, -7, 15, 2],
    [3, -3, 3, -3]
    ]
for l in L:
    print(max_contig_sum(l))