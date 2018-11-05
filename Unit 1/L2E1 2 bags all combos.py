# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 20:57:59 2018

@author: ART
"""

def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(3**N):
        combo1 = []
        combo2 = []
        for j in range(N):
            # test bit jth of integer i
            #print(i, '>>', j, '=', i>>j, ':', '%3==', (i>>j)%2)
            if (i //3**j) % 3 == 1:
                combo1.append(items[j])
            if (i //3**j ) % 3 == 2:
                combo2.append(items[j])
        yield (combo1, combo2)
        
z = yieldAllCombos([1,2,3])
for _ in z:
    print(_)