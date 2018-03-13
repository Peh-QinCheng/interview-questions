from collections import deque, defaultdict

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class LinkNode:
    def __init__(self, node, next=None)
        self.node = node
        self.next = next

class LinkedList:
    def __init__(self, last_node):
        self.last_node = last_node

    def add(self, node)
        self.last_node.next = Node
        self.left_node = node

def make_list(node):
    list = []
    bucket = defaultdict(list)
    DFS(node, -1, bucket)
    for _, v in d.iteritems():
        next = None
        for n in reversed(v):
            link_node = LinkNode(n)
            link_node.next = next
            next = link_node
        list.append(link_node)
    return list


def DFS(node, depth, bucket):
    if node == None:
        return
    bucket[depth+1].append(node)
    DFS(node.left, depth+1, bucket)
    DFS(node.right, depth+1, bucket)