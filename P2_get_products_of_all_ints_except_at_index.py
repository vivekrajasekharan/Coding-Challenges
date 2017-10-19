# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 15:18:54 2017

@author: vivek
"""

X=[1,7,3,4]

def get_products_of_all_ints_except_at_index(List):
    Sol=[]
    for j in range(0,len(List)):
        Prod=1
        for i in range(0,len(List)):
            if i!=j:
                Prod*=List[i]
        Sol.append(Prod)
    return Sol
    
print(get_products_of_all_ints_except_at_index(X))