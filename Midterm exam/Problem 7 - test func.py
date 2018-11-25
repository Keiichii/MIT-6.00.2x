# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 00:02:54 2018

@author: ART
"""

def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    # IMPLEMENT THIS FUNCTION
    a = False
    result = 100
    try: a = test(result) 
    except: pass
    while a == False and (result > -100):
        result -= 1
        try: a = test(result) 
        except: pass
    
    return result


#### This test case prints 49 ####
def f(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))

#### This test case prints 0 ####
def f(x):
    return x == 0
print(solveit(f))

#### This test case prints 3 ####
def f(x):
    return [1,2,3][-x] == 1 and x != 0
print(solveit(f))