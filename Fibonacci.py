# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 20:04:23 2017

@author: vivek
"""

def Fib(n, memo={}):
    if n==0 or n ==1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result= Fib(n-1, memo)+Fib (n-2, memo)
        memo[n]=result
        return result
        
print(Fib(10))