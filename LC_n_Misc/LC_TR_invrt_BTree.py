# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return 0

        stk = []
        stk.append(root)
        while stk:
            child = []
            for node in stk:
                node.left, node.right = node.right, node.left
                if node.left: child.append(node.left)
                if node.right: child.append(node.right)
            stk = child
        return root

# recursive
class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right = root.right, root.left
            if root.left: self.invertTree(root.left)
            if root.right: self.invertTree(root.right)
        return root