class Node:

    # Construct to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return str(self.key)

def find_max_path_sum(root):
    max_sum_between_leaves = 0
    def find_subtree_max_sum(node, max_sum_between_leaves):
        if not node:
            return 0, max_sum_between_leaves
        max_subtree_sum_left, max_sum_between_leaves = find_subtree_max_sum(node.left, max_sum_between_leaves)
        max_subtree_sum_right, max_sum_between_leaves = find_subtree_max_sum(node.right, max_sum_between_leaves)

        max_sum_between_leaves = max(
            max_subtree_sum_left + max_subtree_sum_right + node.key,
            max_subtree_sum_left, max_subtree_sum_right, node.key,
            max_subtree_sum_left + node.key, max_subtree_sum_right+ node.key,
            max_sum_between_leaves
        )
        return max(max_subtree_sum_left + node.key, max_subtree_sum_right + node.key, node.key), max_sum_between_leaves
    _, max_sum_between_leaves = find_subtree_max_sum(root, max_sum_between_leaves)

    return max_sum_between_leaves


def find_max_path_sum_2(root):
    max_sum_between_leaves = 0
    def find_subtree_max_sum(node):
        if not node:
            return 0
        max_subtree_sum_left = find_subtree_max_sum(node.left)
        max_subtree_sum_right = find_subtree_max_sum(node.right)

        nonlocal max_sum_between_leaves

        max_sum_between_leaves = max(
            max_subtree_sum_left + max_subtree_sum_right + node.key,
            max_subtree_sum_left, max_subtree_sum_right, node.key,
            max_subtree_sum_left + node.key, max_subtree_sum_right+ node.key,
            max_sum_between_leaves
        )
        return max(max_subtree_sum_left + node.key, max_subtree_sum_right + node.key, node.key)
    find_subtree_max_sum(root)

    return max_sum_between_leaves

def func():
    enclosing = 'enclosing'
    def inner():
            inner = 'inner'
            print(inner) 
            print(enclosing) 
            print(any) 
    inner()


if __name__ == "__main__":
    root = Node(-15) 
    root.left = Node(5) 
    root.right = Node(6) 
    root.left.left = Node(-8) 
    root.left.right = Node(1) 
    root.left.left.left = Node(2) 
    root.left.left.right = Node(6) 
    root.right.left = Node(3) 
    root.right.right = Node(9) 
    root.right.right.right= Node(0) 
    root.right.right.right.left = Node(4) 
    root.right.right.right.right = Node(-1) 
    root.right.right.right.right.left = Node(10) 
    max_sum = find_max_path_sum_2(root)
    print(max_sum)