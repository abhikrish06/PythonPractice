class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, curr_node, val):
        if val < curr_node.value:
            if curr_node.left:
                self.insert_helper(curr_node.left, val)
            else:
                curr_node.left = Node(val)
        else:
            if curr_node.right:
                self.insert_helper(curr_node.right, val)
            else:
                curr_node.right = Node(val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, curr_node, val):
        if curr_node:
            if curr_node.value == val:
                return True
            elif curr_node.value < val:
                return self.search_helper(curr_node.right, val)
            else:
                return self.search_helper(curr_node.left, val)
        return False

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
