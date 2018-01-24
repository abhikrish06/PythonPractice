# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stk = []
        res = []
        while root or stk:
            if root:
                stk.append(root)
                root = root.left
            else:
                node = stk.pop()
                res.append(node.val)
                root = node.right
        return res


class Solution2:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        else:
            inorder_list = []
            dfs_stack = []
            while True:
                while root:
                    dfs_stack.append(root)
                    root = root.left
                if not dfs_stack:
                    return inorder_list
                node = dfs_stack.pop()
                inorder_list.append(node.val)
                root = node.right