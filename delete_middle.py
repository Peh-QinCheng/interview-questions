class Node:
    def __init__(self):
        self.data = None
        self.next = None

def delete_middle(mid_node):
    # copy data from next node
    # delete next node
    # become the next node
    if mid_node == None or mid_node.next == None:
        return False
    next_node = mid_node.next
    mid_node.data = next_node.data
    mid_node.node = next_node.node
