# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 16:06:02 2017

@author: vivek
"""
import numpy as np
from statistics import mode
class TempTracker:
    def __init__(self):
        self.data=[]
    def insert(self, Val):
        self.data.append(Val)
    def get_T (self):
        return self.data
    def get_max(self):
        return max(self.data)
    def get_min(self):
        return min(self.data)
    def get_mean(self):
        return int(np.mean(self.data))
    def get_mode(self):
        return float(mode(self.data))
        
        
Carmometer=TempTracker()
Carmometer.insert(27)
Carmometer.insert(28)
Carmometer.insert(27)
Carmometer.insert(28)
Carmometer.insert(27)
Carmometer.insert(21)
Carmometer.insert(24)
Carmometer.insert(28)
Carmometer.insert(27)
Carmometer.insert(28)
Carmometer.insert(27)
Carmometer.insert(32)
print (Carmometer.get_mode())