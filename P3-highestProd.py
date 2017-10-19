# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 15:35:30 2017

@author: vivek
"""

list_of_ints=[11,10,9,7,8,5,6,4,2,1]
def highest_prod(List):
    sort_list=sorted(List, reverse=True)
    Prod=sort_list[0]*sort_list[1]*sort_list[2]
    return Prod
    
print (highest_prod(list_of_ints))