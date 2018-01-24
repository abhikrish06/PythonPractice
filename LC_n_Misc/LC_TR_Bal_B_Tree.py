# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stk, res = [], []
        cntL, cntR = 0, 0
        while root or stk:
            if root:
                stk.append(root)
                root = root.left
                cntL += 1
            else:
                node = stk.pop()
                res.append(node.val)
                root = node.right
                cntR += 1
        print(cntL, cntR)
        return True if abs(cntL - cntR) > 1 else False

class Solution2:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def isTrue(root):
            if root is None:
                return 0
            left = isTrue(root.left)
            right = isTrue(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return isTrue(root) != -1