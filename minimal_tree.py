class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def minimal_tree(arr, parent=None):
    print arr
    if not arr:
        return
    if len(arr) == 1 and parent:
        if parent.value > arr[0]:
            parent.left = Node(arr[0])
        else:
            parent.right = Node(arr[0])
    mid = len(arr)/2
    root = arr[mid]
    node = Node(root)
    if parent:
        if parent.value > node.value:
            parent.left = node
        else:
            parent.right = node
    minimal_tree(arr[:mid], node)
    minimal_tree(arr[(mid+1):], node)
    return node


def traverse(node):
    print("root: %d" % node.value)
    if node.left:
        print("left: %d" % node.left.value)
    if node.right:
        print("right: %d" % node.right.value)
    if node.left:
        traverse(node.left)
    if node.right:
        traverse(node.right)
node = minimal_tree([1,2,3,4])
traverse(node)
