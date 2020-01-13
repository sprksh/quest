class newNode:

    # Construct to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

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
    max_sum_path = [root]

    # base case
    def traverse(node):
        if node is None:
            return 0

        l = traverse(node.left)
        r = traverse(node.right)
        if l > r:
            max_sum_path.append(node.left)
            return node.key + l
        if r > l:
            max_sum_path.append(node.right)
            return node.key + r

    max_path_sum = traverse(root)
    return (max_path_sum, max_sum_path)


if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(6)
    root.right.right = newNode(7)
    root.right.left.right = newNode(8)

    sum = max_path_sum(root)

    print(sum)