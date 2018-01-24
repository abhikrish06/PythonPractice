# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        elif not root.left and not root.right:
            return True
        elif not root.left and root.right:
            return False
        elif root.left and not root.right:
            return False
        else:
            nodeL, nodeR = root.left, root.right
            if nodeL.val != nodeR.val:
                return False
            if nodeL:
                stkL, resL = [], []
                while nodeL or stkL:
                    if nodeL:
                        stkL.append(nodeL)
                        nodeL = nodeL.left
                    else:
                        node1 = stkL.pop()
                        resL.append(node1.val)
                        nodeL = node1.right
            if nodeR:
                stkR, resR = [], []
                while nodeR or stkR:
                    if nodeR:
                        stkR.append(nodeR)
                        nodeR = nodeR.right
                    else:
                        node2 = stkR.pop()
                        resR.append(node2.val)
                        nodeR = node2.left
            print(resL, resR)
            if resL == resR:
                return True
            else:
                return False

# simple recursive solns
def isSymmetric(self, root):
    def isSym(L, R):
        if L and R and L.val == R.val:
            return isSym(L.left, R.right) and isSym(L.right, R.left)
        return L == R
    return isSym(root, root)

# iterative
def isSymmetric(self, root):
    queue = [root]
    while queue:
        values = [i.val if i else None for i in queue]
        if values != values[::-1]: return False
        queue = [child for i in queue if i for child in (i.left, i.right)]
    return True