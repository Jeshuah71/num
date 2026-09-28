class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Stack: 
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1 
        
    def push(self, value):
        new_node = Node(value)
        if self.height ==0:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height +=1
        return True
    
    def pop(self):
        if self.height == 0:
            return None
        
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1 
        return temp
    

class NodeQueue:
    def __init__(self, value):
        self.value = value
        self.next = None 
        
class Queue:
    
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1 
        

    def enqueue(self, value):
        
        new_node = Node(value)
        if self.length  == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1 
        return True
    
    def dequeque(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            
            self.first = self.first.next
            temp.next = None
        self.length == 1 
        return temp 
    
    
# Stack implement using a list 

    def __init__(self):
        self.stack_list = []
        

# def check stack is empty
    def is_empty(self):
        return len(self.stack_list) == 0
# print stack that uses lists 

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])
                
    
    def push(self, value):
        self.stack_list.append(value)
        
    # def pop a satck list
    
    def pop(self):
        if len(self.stack_list) == 0:
            return None
        
        return self.stack_list.pop()
    
    
    def reverse_string(string):
        stack = Stack()
        
        # Put each character into the tack
        for char in string:
            stack.push(char)
        
        reversed_string = ""
        
        # Take characters out of the stack
        # they come out in refverse order
        while not stack.is_empty():
            reversed_string += stack.pop()
        
        return reversed_string

    

def is_balanced_parenthesis(parentheses):
    stack = Stack()
    
    for char in parentheses:
        if char == "(":
            stack.push(char)
        else:
            if stack.is_empty():
                
                return False
            stack.pop()
    return stack.is_empty
        
    
class Myqueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, value):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
            
        self.stack1.append(value)
        
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
            

    def dequeue(self):
        if len(self.stack1) == 0:
            return None
        
        return self.stack1.pop()
    
