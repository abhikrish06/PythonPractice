# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left or not root.right:
            return (self.minDepth(root.left)+self.minDepth(root.right))+1
        return min(self.minDepth(root.left)+self.minDepth(root.right))+1

# alternate way using map function
# for more info on map-filter-reduce, visit: http://www.bogotobogo.com/python/python_fncs_map_filter_reduce.php

    def minDepth(self, root):
        if not root: return 0
        d = map(self.minDepth, (root.left, root.right))
        return 1 + (min(d) or max(d))