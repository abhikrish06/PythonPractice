

def get_cheapest_cost(rootNode):
    min_val = 1000000
    if rootNode.children:
        for child in rootNode.children:
            val = self.get_cheapest_cost(child)
            if val < min_val:
                min_val = val
    else:
        return rootNode.cost

    return min_val + rootNode.cost


##########################################
# Use the helper code below to implement #
# and test your function above           #
##########################################

# A node

class Node:

    # Constructor to create a new node
    def __init__(self, cost):
        self.cost = cost
        self.children = []
        self.parent = None


def get_cheapest_cost(rootNode):
    min_val = 1000000
    if rootNode.children:
        for child in rootNode.children:
            val = self.get_cheapest_cost(child)
            if val < min_val:
                min_val = val
    else:
        return rootNode.cost

    return min_val + rootNode.cost


def get_cheapest_cost(rootNode):
    if not rootNode.children:
        return rootNode.cost
    else:
        return min(get_minimum_in_subtree(node) + rootNode.cost for node in rootNode.children)
