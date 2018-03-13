class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def sum_list(node1, node2):
    arr = []
    bring_over = 0
    cur_node1 = node1
    cur_node2 = node2
    while(cur_node1 != None or cur_node2 != None):
        if cur_node1 == None:
            arr.append(cur_node2.data + bring_over)
            bring_over = 0
            cur_node2 = cur_node2.next
        elif cur_node2 == None:
            arr.append(cur_node1.data + bring_over)
            bring_over = 0
            cur_node1 = cur_node1.next
        else:
            sum = cur_node1.data + cur_node2.data + bring_over
            bring_over = (sum - (sum % 10))/10
            arr.append(sum % 10)
            cur_node1 = cur_node1.next
            cur_node2 = cur_node2.next
    nodes_arr = [make_node(i) for i in arr]
    for n in range(len(nodes_arr)):
        if n + 1 == len(nodes_arr):
            break
        nodes_arr[n].next = nodes_arr[n + 1]
    return nodes_arr[0]

def make_node(i):
    node = Node()
    node.data = i
    return node
        