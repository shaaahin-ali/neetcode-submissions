# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
     count = 0
     if not root:
        return 0
     else:
        
        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)
     return 1 + max(left ,right)
        

    
    