# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inOrder(self, root, lst):
        """
        :param root: Treenode
        :param lst: list
        :return: list
        """
        if not root:
            return []
        else:
            self.inOrder(root.left)
            lst.append(root.val)
            self.inOrder(root.right)
        return lst

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        min_val = float("Inf")
        lst = self.inOrder(root, [])
        for i in range(1, len(lst)):
            min_val = min(min_val, lst[i] - lst[i-1])
        return min_val
