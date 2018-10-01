# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depth = 1

        def find_depth(node):
            if not node: return 0
            L = find_depth(node.left)
            R = find_depth(node.right)
            self.depth = max(self.depth, L + R + 1)
            return max(L, R) + 1

        find_depth(root)
        return self.depth - 1