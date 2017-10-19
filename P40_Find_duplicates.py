# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 19:00:37 2017

@author: vivek
"""

Integers=list(range(1,31))

Int2=[29,30,45,66,66,66,8,66,6,7,12,16,17,17]



def find_unique(List1, List2):
    Inti=List1+List2    
    Unique=list(set(Inti))
    Mult_int=[]
    for i in Unique:
        if Inti.count(i)>1:
            Mult_int.append(i)
    return Mult_int
    
print(find_unique (Integers, Int2))
        