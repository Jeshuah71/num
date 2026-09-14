# Find k in 

def find_kth_from_end(ll, k):
    slow = ll.head
    fast = ll.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    while fast is not None:
        slow = slow.next
        fast = fast.next
    return slow

# Binary to decimay 

def binary_to_decimal(self):
    current = self.head
    decimal = 0
    
    while current is not None:
        decimal = decimal * 2 + current.value
        current = current.next
    return decimal

 
#  def binary_to_decimal(self):
#     current = self.head
#     decimal = 0
    
#     while current is not None:
#         decimal = decimal * 2 + current.value
#         current = current.next
#     return decimal

def partition_list(self, x):
    if self.head is None:
        return
    
    dummy1 = Node(0)
    dummy2 = Node(0)
    
    prev1 = dummy1
    prev2 = dummy2
    
    current = self.head
    
    while current is not None:
        if current.value < x:
            prev1.next = current
            prev1 = current
        else:
            prev2.next = current
            prev2 = current
        current = current.next
    
    prev2.next = None
    prev1.next = dummy2.next
    
    self.head = dummy1.next
    

def reverse_between(self, start_index, end_index):
    if self.head is None or start_index.next is None:
        return None
    
    dummy = Node(0)
    dummy.next = self.head
    
    before_start = dummy
    
    for _ in range(start_index):
        before_start = before_start.next
    
    current = before_start.next
    previous = None
    
    for _ in range(end_index - start_index + 1):
        temp = current.next
        current.next = previous
        previous = current
        current = temp
    
    before_start.next.next = current
    before_start.next = previous
    
    self.head = dummy.next
    


# Double linked list exercises like leetcode exercises

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def is_palindrome(self):
        forward = self.head
        backward = self.tail
        
        for _ in range(self.legth // 2):
            if forward.value != backward.value:
                return False
            forward = forward.next
            backward = backward.prev
        return True

    def reverse(self):
        current = self.head
        
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            
            current = current.prev
        temp = self.head
        self.head = self.tail
        self.tail = temp



my_dll_1 = DoublyLinkedList(1)
my_dll_1.append(2)
my_dll_1.append(3)
my_dll_1.append(2)
my_dll_1.append(1)

print('my_dll_1 is_palindrome:')
print( my_dll_1.is_palindrome() )


my_dll_2 = DoublyLinkedList(1)
my_dll_2.append(2)
my_dll_2.append(3)

print('\nmy_dll_2 is_palindrome:')
print( my_dll_2.is_palindrome() )



"""
    EXPECTED OUTPUT:
    ----------------
    my_dll_1 is_palindrome:
    True

    my_dll_2 is_palindrome:
    False

"""

