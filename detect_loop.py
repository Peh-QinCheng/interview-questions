from collections import defaultdict

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def detect_loop(node):
    freq_table = defaultdict(int)
    while(node.next != None):
        freq_table[id(node)] += 1
        if freq_table[id(node)] > 1:
            return node
        node = node.next
    return None


nodea = Node()
nodeb = Node()
nodec = Node()
noded = Node()
nodea.next = nodeb
nodeb.next = nodec
nodec.next = noded
noded.next = nodea
nodee = Node()
nodee.next = nodea
print nodea
print detect_loop(nodee)