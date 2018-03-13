class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def intersect(nodea,nodeb):
    pointer_a = nodea
    pointer_b = nodeb

    len_a = 0
    len_b = 0
    while pointer_a.next != None or pointer_b.next != None:
        if pointer_a.next != None:
            len_a += 1
            pointer_a = pointer_a.next
        if pointer_b.next != None:
            len_b += 1
            pointer_b = pointer_b.next

    if pointer_a == pointer_b:
        if len_a == len_b:
            return find_intersect(nodea, nodeb)
        else:
            if len_a > len_b:
                shorter = nodeb
                longer = nodea
            else:
                longer = nodeb
                shorter = nodea
            longer = chop_list(longer, abs(len_a - len_b))
            return find_intersect(longer, shorter)
    else:
        return False

def chop_list(node, diff):
    counter = 0
    while node.next != None:
        counter += 1
        node = node.next
        if counter == diff:
            return node
    return node
        
def find_intersect(nodea, nodeb):
    while nodea.next != None or nodeb.next != None:
        if nodea == nodeb:
            return nodea
        else:
            nodea = nodea.next
            nodeb = nodeb.next
    return None


node_star = Node()
common_chain = Node()
pointer = common_chain
for i in range(5):
    pointer.next = Node()
    pointer = pointer.next
node_star.next = common_chain
start_chain1 = Node()
pointer = start_chain1
for i in range(3):
    pointer.next = Node()
    pointer = pointer.next
pointer.next = node_star
start_chain2 = Node()
pointer = start_chain2
for i in range(1):
    pointer.next = Node()
    pointer = pointer.next
pointer.next = node_star

# while(start_chain2.next != None):
#     print start_chain2
#     start_chain2 = start_chain2.next
# print "CHAIN 2\n"
# while(start_chain1.next != None):
#     print start_chain1
#     start_chain1 = start_chain1.next

# print "BREAK"
print node_star
# # print node_star.next
# # print common_chain
print intersect(start_chain1, start_chain2)