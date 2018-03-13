from stack_min import Stack

def sort_stack(stack):
    new_stack = Stack([])
    while(not stack.is_empty()):
        temp = stack.pop()
        if new_stack.is_empty():
            new_stack.push(temp)
            continue
        while new_stack.peek() > temp:
            stack.push(new_stack.pop())
        if temp >= new_stack.peek():
            new_stack.push(temp)
    while(not new_stack.is_empty()):
        stack.push(new_stack.pop())
    return stack

def sort_stack2(stack):
    new_stack = Stack([])
    while(not stack.is_empty()):
        temp = stack.pop()
        if new_stack.is_empty():
            new_stack.push(temp)
            continue
        while new_stack.peek() < temp:
            stack.push(new_stack.pop())
        if temp <= new_stack.peek():
            new_stack.push(temp)
    # while(not new_stack.is_empty()):
    #     stack.push(new_stack.pop())
    return new_stack

stack = Stack([1,2,3,4])
new_stack = sort_stack(stack)
print new_stack.values
print new_stack.pop()