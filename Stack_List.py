class Stack:
    def __init__(self):
        self.stack_list = []
        
    def push(self, value):
        self.stack_list.append(value)
        
    def pop(self, value):
        if len(self.stack_list) == 0:
            return None
        
        return self.stack_list.pop()
    
    def is_empty(self):
        return len(self.stack_list) == 0
    
    def reverse_string(string):
        stack = Stack()
        
        for char in string:
            stack.push(char)
        
        reversed_string = ""
        
        while not stack.is_empty():
            reversed_string += stack.pop()
        
        return reversed_string
    
    
    def is_balanced_parentheses(parentheses):
        stack = Stack()
        
        for char in parentheses:
            if char == "(":
                stack.push(char)
            else:
                if stack.is_empty():
                    return False
                stack.pop()
        return stack.is_empty()
    
    def sort_stack(stack):
        sorted_stack = Stack()
        
        while not stack.is_empty():
            temp = stack.pop()
        
            while not sorted_stack.is_empty() and sorted_stack.peek() > temp:
                stack.push(sorted_stack.pop())
        
            sorted_stack.push(temp)
        while not sorted_stack.is_empty():
            stack.push(sorted_stack.pop())
            
        
            
    
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    # Equeue method
    
    def enqueue(self, value):
        while len(self.stack1)> 0:
            self.stack2.append(self.stack1.pop())
        
        self.stack1.append(value)
        
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
    
    def dequeue(self):
        if len(self.stack1) == 0:
            return None
        return self.stack1.pop()
    
    def peek(self):
        return self.stack1[-1]
    
    
    def is_empty(self):
        return len(self.stack1) == 0
    