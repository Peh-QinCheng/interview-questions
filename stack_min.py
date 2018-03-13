class Stack:
    def __init__(self, values):
        self.values = values

    def push(self,value):
        self.values.append(value)
    
    def pop(self):
        return self.values.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.values[-1]
    
    def is_empty(self):
        return not bool(self.values)

class StackMin:
    def __init__(self):
        self.stack = Stack([])
        self.stack_min = Stack([])

    def push(self, value):
        self.stack.push(value)
        if self.stack_min.is_empty():
            self.stack_min.push(value)
        elif value <= self.stack_min.peek():
            self.stack_min.push(value)
    
    def pop(self):
        if self.peek() == self.stack_min.peek():
            self.stack_min.pop()
        return self.stack.pop()
        

    def peek(self):
        return self.stack.peek()
    
    def min(self):
        return self.stack_min.peek()

# stack = StackMin()
# test_data = [4,3,5,6,1,1]
# for i in test_data:
#     stack.push(i)

# for _ in test_data:
#     print stack.min()
#     print stack.pop()
#     print '\n'