"""
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the
square brackets is being repeated exactly k times. Note that k is guaranteed
to be a positive integer.

You may assume that the input string is always valid; No extra white spaces,
square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits
and that digits are only for those repeat numbers, k.
For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

Source: https://leetcode.com/problems/decode-string/#/description
"""


# DO NOT CHANGE THIS CLASS
class Solution(object):
	#YOUR CODE GOES HERE
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst=list(s)
        wlist=""
        mf=1
        wrd=""
        wod=""
        lst2=""
        while len(lst)>0:
            
            wrd=""
            wod=""
            a=lst.pop(0)
            if a.isdigit():
                mf=int(a)
            elif a == "[":
                
                wrd=""
                while a!="]":
                    a=lst.pop(0)
                    wrd=wrd+a
                    
                #lst.pop(0)
                if "[" in wrd:
                    lst2=wrd
                wrd=wrd[:-1]
            else:
                wod=""
                wod=wod+a
            if len(lst2)==0:
                wlist=wlist+wrd*mf+wod
            else: 
                lst = list(mf*lst2)
                lst2=""   
        return (wlist)                                  


# Please add your test cases below:
s1 = "3[a]2[bc]"
s2 = "3[a2[c]]"
s3 = "2[abc]3[cd]ef"

obj=Solution()
so1=obj.decodeString(s1)
so2=obj.decodeString(s2)
so3=obj.decodeString(s3)
print ("""Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".""")
    
print (s1, "returns", so1)
print (s2, "returns", so2)
print (s3, "returns", so3)