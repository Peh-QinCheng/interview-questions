class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def ll_palindrome(node):
    length = 0
    cur_node = node
    while(cur_node != None):
        length += 1
        cur_node = cur_node.next
    if length % 2 == 0:
        return check_palindrome(node)
    else:
        node = remove_middle_node(node, length)
        return check_palindrome(node)


def check_palindrome(node):
    chars = []
    while(node.next != None):
        if node.data in chars:
            if chars.pop() == node.data:
                continue
            else: 
                return False
        else:
            chars.append(node)
        node = node.next
    return True

def remove_middle_node(node, length):
    index = length/2
    counter = 0
    cur_node = node
    while(node.next != None):
        if counter == index:
            cur_node.data = cur_node.next.data
            cur_node.next = cur_node.next.next
            break
        counter += 1
        cur_node = cur_node.next
    return node

nodea = Node('a')
nodeb = Node('b', nodea)
nodea2 = Node('a', nodeb)
print ll_palindrome(nodea2)
