class Node:
    def __init__(self, children, value):
        self.children = children
        self.value = value
        self.visited = False

def DFS(start, end, results=[]):
    start.visited = True
    if start == end:
        results.append(True)
        return
    elif not start.children: #check if empty, [] is falsey
        results.append(False)
        return
    for c in start.children:
        if not c.visited:
            DFS(c, end, results)
        else:
            results.append(False) # tbh this line doesn't really matter
    return True in results

def make_children(node, level):
    if level == 0:
        return None
    for i in range(2):
        child = Node([], str(level) + str(i))
        node.children.append(child)
    for c in node.children:
        make_children(c, level-1)

# start_node = Node([], "root")
# make_children(start_node, 2)
# end_node = start_node.children[-1].children[-1]
# results = []
# start_node.children[-1].children[0].children.append(start_node.children[-1])
# print DFS(start_node, end_node, results)
# print results


    
