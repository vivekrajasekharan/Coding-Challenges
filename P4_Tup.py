# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 15:45:30 2017

@author: vivek
"""

meetings=[(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
 
def merge_ranges(meetings):

    sorted_meetings=sorted (meetings)
    merged_meetings=[sorted_meetings[0]]
    for i,j in sorted_meetings[1:]:
        k,l=merged_meetings[-1]
        if i<=l:
            merged_meetings[-1]=(k,max(j,l))
            
        else:
            merged_meetings.append((i,j))
    return merged_meetings
        
print(merge_ranges(meetings))