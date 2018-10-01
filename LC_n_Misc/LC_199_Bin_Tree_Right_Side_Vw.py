# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        def helper(node, depth):
            if not node: return
            if depth > len(res):
                res.append(node.val)
            if node.right:
                helper(node.right, depth+1)
            if node.left:
                helper(node.left, depth+1)
        helper(root, 1)

        return res
