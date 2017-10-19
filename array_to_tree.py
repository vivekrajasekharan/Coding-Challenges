"""
Given an array where elements are sorted in ascending order,
convert it to a height balanced BST.

Source: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/#/description
"""
import numpy as np

# Constructor for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# DO NOT CHANGE THIS CLASS
class Solution(object):
    def sortedArrayToBST(self, nums):
    	#YOUR CODE GOES HERE
    	##
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return None
        


        
    def arr2tree (self, arr, left, right):
        if left > right:
            return None
        mid=(left+right)//2
        BST=TreeNode(arr[mid])
        BST.left=self.arr2tree (arr, left, mid-1)
        BST.right = self.arr2tree (arr, mid+1, right )
               
        return BST
               
            
        



#Please come up with your own testcases below:
myarray = np.array(range(1,7))
mylist=myarray.tolist()
print (mylist)
answer=Solution()
tree=answer.arr2tree(mylist, 0, len(mylist)-1)
print ("                   ", tree.val)
print ("    ",tree.left.val,"                   ""           ", tree.right.val)
print (tree.left.right.val,"                   ","           ", tree.right.left.val,"   ", tree.right.right.val)