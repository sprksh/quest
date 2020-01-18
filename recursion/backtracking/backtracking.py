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

def n_queens(n):
    # backtracking
    pass


def tree_sum(root):
    if root is None:
        return 0
    return root.key + tree_sum(root.left) + tree_sum(root.right)


def max_path_sum(root):
    # base case
    def sub_tree_sum(node):
        if node is None:
            return 0
        l = sub_tree_sum(node.left)
        r = sub_tree_sum(node.right)
        return node.key + l if l > r else node.key + r

    max_path_sum = sub_tree_sum(root)
    return max_path_sum


def max_sum_path(root):
    # needs to return path, no idea how
    # this page contains a solution but try
    # https://www.techiedelight.com/find-maximum-sum-root-to-leaf-path-binary-tree/
    def sub_tree_sum(node):
        if node is None:
            return 0
        l = sub_tree_sum(node.left)
        r = sub_tree_sum(node.right)
        return node.key + l if l > r else node.key + r

    max_path_sum = sub_tree_sum(root)
    return max_path_sum


if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(6)
    root.right.right = newNode(7)
    root.right.left.right = newNode(12)

    sum = max_path_sum(root)

    print(sum)