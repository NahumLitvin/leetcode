
# Definition for a binary tree node.
# https://leetcode.com/problems/balanced-binary-tree/submissions/
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tallest_leaf_height(self, root: Optional[TreeNode], height : int):
        if height == -1:
            return -1
        if root is None:
            return height
        left = self.tallest_leaf_height(root.left, height +1)
        right= self.tallest_leaf_height(root.right, height +1)
        if abs(left - right) > 1:
            return -1
        return max(left,right) 
     

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.tallest_leaf_height(root,0) != -1
        
            
            
        