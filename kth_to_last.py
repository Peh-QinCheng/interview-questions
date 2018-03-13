class Node:
    def __init__(self):
        self.data = None
        self.next = None
# recursion
def kth_to_last(node, counter, k):
    if node.next == None:
        return [node, counter + 1]
    val = kth_to_last(node.next, 0, k)
    if isinstance(val, Node):
        return val
    elif val[1] == k:
        return val[0]
    else:
        return [node, val[1] + 1]
# iterative
def kth_to_last(node, k):
    first = node
    second = node
    for _ in range(k):
        first = first.next
    while(first.next != None):
        first = first.next
        second = second.next
    return second

