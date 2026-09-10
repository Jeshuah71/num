head = {
            "value": 11,
            "next": {
                "value": 3,
                "next": {
                    "value": 23,
                    "next": {
                        "value": 7,
                        "next": None
                    }
                }
            }
        }

print(head['next']['next']['value'])  # Output: 23

# class definition for Node so we don't have to create a node 4 times 




class Node:
    # constructor method to initialize the value and next attributes
    def __init__(self, value):
        # self = the instance of the class that is being created
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value) # this create the node
        self.head = new_node # this is the head of the linked list point to the same node 
        self.tail = new_node # this is the tail of the linked list point the same Node 
        self.length = 1 # this is the length of the linked list
    
    # method to print the values of the list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    # self helps us to say that this is a  method instead of a function 
    def append(self, value):
        new_node = Node(value) # this create the node
        if self.length == 0: # is this list empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node    
            self.length += 1
        return True # this is optional but it is a good practice to return something from a method 
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
        
    
      

my_linked_list = LinkedList(4)

my_linked_list.append(5)

my_linked_list.print_list()  # Output: 4, 5

print(my_linked_list.head.value)  # Output: 4
    # def insert(self, index, value):
    #     # Create new Node and insert the Node 
    
    # (2) Items - Returns 2 Node
print(my_linked_list.pop())

    # Output: 5
print(my_linked_list.pop())

print(my_linked_list.pop())  # Output: None

# example usage of the prepend method
my_linked_list.prepend(3)
my_linked_list.print_list()  # Output: 3, 4

