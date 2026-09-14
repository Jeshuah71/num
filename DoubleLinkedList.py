class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class DoubleLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1 


    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        # can be if temp is not None or if temp: both are same
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
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp
              
my_double_linked_list = DoubleLinkedList(1)
my_double_linked_list.append(2)

# (2) Items - Returns 2 Node
print(my_double_linked_list.pop_first())
# (1) Item -  Returns 1 Node
print(my_double_linked_list.pop_first())
# (0) Items - Returns None
print(my_double_linked_list.pop_first())


# (2) Items - Returns 2 Node
print(my_double_linked_list.pop())

# (1) Item -  Returns 1 Node
print(my_double_linked_list.pop())

# (0) Items - Returns None
print(my_double_linked_list.pop())




my_double_linked_list = DoubleLinkedList(0)
my_double_linked_list.append(1)
my_double_linked_list.append(2)
my_double_linked_list.append(3)


print(my_double_linked_list.get(0).value)  # Output: 0
print(my_double_linked_list.get(1).value)  # Output: 1
print(my_double_linked_list.get(2).value)  # Output: 2
print(my_double_linked_list.get(3).value)  # Output: 3

my_double_linked_list.set_value(1, 10)
print(my_double_linked_list.get(1).value)  # Output: 10

my_double_linked_list.insert(2, 20)
print(my_double_linked_list.get(2).value)  # Output: 20

# remove the node at index 1
removed_node = my_double_linked_list.remove(1)
print(removed_node.value)  # Output: 10

