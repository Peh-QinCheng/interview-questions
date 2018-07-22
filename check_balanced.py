class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_balanced(root, results=[]):
    set_height(root)
    not_balanced = check_height_diff(root)
    return not not_balanced

def check_height_diff(node, results=[]):
    if not node:
        return
    left_height = node.left.value if node.left else 0
    right_height = node.right.value if node.right else 0
    if abs(left_height - right_height) > 1:
        results.append(False)

    check_height_diff(node.left, results)
    check_height_diff(node.right, results)

    return False in results


def set_height(node):
    if not node:
        return 0
    if node.left == None and node.right == None:
        node.value = 0
        return node.value

    left_height = set_height(node.left)
    right_height = set_height(node.right)
    if left_height > right_height:
        height = left_height + 1
    else:
        height = right_height + 1
    node.value = height
    return height


def make_tree(node, height):
    if height == 0:
        return
    node.left = Node()
    node.right = Node()
    make_tree(node.left, height - 1)
    make_tree(node.right, height - 1)

start_node = Node()
make_tree(start_node, 3)
start_node.left = None
print is_balanced(start_node)