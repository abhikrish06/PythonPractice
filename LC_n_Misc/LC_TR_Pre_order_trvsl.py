# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        else:
            preorder_list = []
            dfs_stack = []
            dfs_stack.append(root)
            while(dfs_stack != []):
                node = dfs_stack.pop()
                preorder_list.append(node.val)
                if node.right:
                    dfs_stack.append(node.right) # pre order traversal is node then left then right. so right is pushed
                                                 # into stack first so that left is processed first
                if node.left:
                    dfs_stack.append(node.left)
            return preorder_list