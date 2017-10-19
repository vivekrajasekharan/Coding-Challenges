# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 15:07:18 2017

@author: vivek
"""

files = {
    'Input.txt': 'Randy Savage',
    'Code.py': 'Stan Lee',
    'Output.txt': 'Randy Savage',
    'Toodle-doo.mpg':'Boxer McBoxer Face',
    'Kill Bill Vol-2.mpg': 'Stan Lee',
    'Deadpool.mpg':'Stan Lee',
    'Coding-for-dummies.pdf':'Boxer McBoxer Face',
    
}
Key=[]
Value=[]
for k,v, in files.items():
    Key.append(k)
    Value.append(v)
Users=set(Value)
for i in Users:
    for k,v, in files.items():    
        if v==i:
            print (v,"owns", k)        