class Node:
    def __init__(self):
        self.data = None
        self.next = None

def partition(node, x):
    # Store all nodes
    # Sort them by their value
    # link them tgt
    nodes = []
    cur = node
    while(cur.next != None):
        nodes.append(cur)
        cur = cur.next
    nodes.sort(key=lambda z:z.data)
    for n in range(len(nodes)):
        if n + 1 == len(nodes):
            break
        nodes[n].next = nodes[n+1]
    return nodes

def partition(node, x):
    small = []
    big = []
    cur = node
    while(cur.next != None):
        if cur.data < x:
            small.append(cur)
        else:
            big.append(cur)
        cur = cur.next
    for n in range(len(small)):
        if n + 1 == len(small):
            break
        small[n].next == small[n+1]
    for n in range(len(big)):
        if n + 1 == len(big):
            break
        big[n].next == big[n+1]
    small[-1].next = big[0]
    return small