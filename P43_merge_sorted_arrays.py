# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 18:56:03 2017

@author: vivek
"""

def merge_lists(A,B):
    return sorted(A+B)   


my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]
print (merge_lists(my_list, alices_list))
