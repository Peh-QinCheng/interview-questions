from collections import defaultdict

class node:
    def __init__(self):
        self.data = None
        self.next = None
class linked_list:
    def __init__(self):
        self.cur_node = None
    
    def add_node(self, data):
        new_node = node()
        new_node.data = data
        new_node.next = self.cur_node
        self.cur_node = new_node

def remove_dups(node):
    freq_table = defaultdict(int)
    previous = None
    n = node
    while(n != None):
        if freq_table[n.data] != 0:
            previous.next = n.next
        else:
            freq_table[n.data] += 1
            previous = n
        n = n.next

def remove_dups2(node):
    current  = node
    runner  = node
    while(current.next != None):
        while(runner.next != None):
            if (current.data == runner.next.data):
                current.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    
