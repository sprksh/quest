"""
Backtracking is when you backtrack after recursion
Examples in n_queens in the bottom section
"""


class newNode:

    # Construct to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return str(self.key)

def tree_sum(root):
    if root is None:
        return 0
    return root.key + tree_sum(root.left) + tree_sum(root.right)



# this is plain recursion

def max_path_sum(root):
    def sub_tree_sum(node):
        # base case
        if node is None:
            return 0
        l = sub_tree_sum(node.left)
        r = sub_tree_sum(node.right)
        return node.key + l if l > r else node.key + r

    max_path_sum = sub_tree_sum(root)
    return max_path_sum 


def max_sum_path(root):
    actual_path = []
    def sub_tree_sum(node):
        if node is None:
            return 0
        l = sub_tree_sum(node.left)
        r = sub_tree_sum(node.right)
        
        maximum = node.key + l if l > r else node.key + r
        actual_path.append(node.left if l > r else node.right)
        
        return maximum

    max_path_sum = sub_tree_sum(root)
    actual_path = [_ for _ in actual_path if _]
    actual_path.append(root)
    return max_path_sum, actual_path


if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(6)
    root.right.right = newNode(7)
    root.right.left.right = newNode(12)

    max_sum, path = max_sum_path(root)

    print(max_sum, path)