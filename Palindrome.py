# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 14:54:07 2017

@author: vivek
"""

def palindrome(word):
    Letter_list =list(word)
    if Letter_list[::-1]==Letter_list:
        return "Palindrome!"
    else:
        return "DO YOU EVEN PALINDROME BRO?"
        
print(palindrome("malayali"))