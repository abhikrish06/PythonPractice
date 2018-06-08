# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sm):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right and root.val == sm:
            return True
        else:
            return self.hasPathSum(root.left, root.val - sm) or self.hasPathSum(root.right, root.val - sm)


obj = Solution()
print(obj.hasPathSum([5, 4, 8, 11, 'Null', 13, 4, 7, 2, 'Null', 'Null', 'Null', 1], 22))
