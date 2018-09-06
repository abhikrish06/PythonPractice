# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inOrderTrvsl(self, node, lst):
        if not node:
            return []
        else:
            self.inOrderTrvsl(node.left, lst)
            lst.append(node.val)
            self.inOrderTrvsl(node.right, lst)
        return lst

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        min_diff = float("inf")
        lst = self.inOrderTrvsl(root, [])
        for i in range(1, len(lst)):
            min_diff = min(min_diff, lst[i] - lst[i - 1])
        return min_diff