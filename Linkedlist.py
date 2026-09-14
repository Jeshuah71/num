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
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    # we can use temp.value to get the value of the node and temp.next to get the next node in the linked list
    
    def get(self, index):
        # check if the index is valid
        if index < 0 or index >= self.length:
            return None
        # traverse the linked list to find the node at the given index
        temp = self.head
        # loop through the linked list until we reach the desired index
        for _ in range(index):
        # we only use i if we are going to use that variable inside of the for loop so if is not used jsut leave _ 
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        # variable pointing to the node before the index where we want to insert the new node
        temp = self.get(index -1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    # very important
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        
# example of reverse method

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.reverse()
my_linked_list.print_list()  # Output: 4, 3, 2,1


    
    
# example of remove method
my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

print(my_linked_list.remove(2))  # Output: Node with value 3

my_linked_list.print_list()    
    
# example of insert method    
    
my_linked_list = LinkedList(0)
my_linked_list.append(2)

my_linked_list.insert(1, 1)

my_linked_list.print_list()  # Output: 0, 1,2



# example of set_value method

my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

my_linked_list.set_value(1,4)

my_linked_list.print_list()  # Output: 11, 4, 23, 7    
    
# example of get method
my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

print(my_linked_list.get(2))  # Output: 2


# example of pop_first method

my_linked_list = LinkedList(4)
my_linked_list.append(5)


# (2) Items - Returns 2 Node
print(my_linked_list.pop_first())
# (1) Item - Returns 1 Node
print(my_linked_list.pop_first())
# (0) Items - Returns None
print(my_linked_list.pop_first())


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

