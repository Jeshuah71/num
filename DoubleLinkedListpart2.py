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
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
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
        before = self.get(index -1)
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
        if index == self.length -1:
            return self.pop()
        
        temp = self.get(index - 1)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next 
        temp.next = None
        temp.prev = None
        
        self.length -=1 
        return temp
    
    # find palindrome in a double link list
    
    def is_palindrome(self):
        left = self.head
        right = self.head
        
        while left != right and left.prev != right:
            
            if left.value != right.value:
                return False
            
            left = left.next
            right = right.prev
        return True
    
    # reverse double linked list 
    def reverse(self):
        current = self.head
        
        while current:
            temp = current.next
            
            current.next = current.prev
            current.prev = temp 
            
            current = temp 
        self.head, self.tail = self.tail, self.head
        
    def partition_list(self, x):
        if self.head is None:
            return
        
        dummy1 = Node(0)
        dummy2 = Node(0)
        
        less = dummy1
        greater = dummy2
        
        current = self.head
        
        while current:
            next_node = current.next
            
            if current.value < x:
                less.next = current 
                current.prev = less
                less = current
            else:
                greater.next = current
                current.prev = greater
                greater = current
            current = next_node
            
        less.next = dummy2.next
        
        if dummy2.next:
            dummy2.next.prev = less
        
        self.head = dummy1.next
        
        if self.head:
            self.head.prev = None
        
        if dummy2.next:
            self.tail = greater
        else:
            self.tail = less
            
        self.tail.next = None
    
    def reverse_between(self, start_index, end_index):
        
        # if the list is empty, has one node,
        # or we are reversing only one position,
        # there is nothing to do
        if self.head is None or self.head == self.tail or start_index == end_index:
            return 
        
        # start at the head
        current = self.head
        
        # Move current to the node at the start index
        for _ in range(start_index):
            current = current.next 
            
        # Save the first node of the section 
        start_node = current
        
        # Save the node BEFORE the section
        before = start_node.prev
        
        # This will eventually become 
        # the new first node of the reversed section
        new_section_head = None
        
        # Reverse all nodes form start_idex to end_index
        for _ in range(end_index - start_node + 1):
            
            # Save where we originally needed to go next
            next_node = current.next
            
            # Swap next and prev
            current.next = current.prev
            current.prev = next_node
            
            # Remember the most recently reversed node
            new_section_head = current
            
            # Move through the ORIGINAL list 
            current = next_node 
            
        # current is now the node AFTER the reversed section 
        after = current 
        
        # Connext the left side 
        if before:
            before.next = new_section_head
        
        else:
            # Reversal started at index 0
            self.head = new_section_head
        
        new_section_head.prev = before
        
        # Connect the right side
        start_node.next = after
        
        if after:
            after.prev = start_node
        else:
            self.tail = start_node
                
        
        
my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.append(8)
my_doubly_linked_list.append(9)

my_doubly_linked_list.prepend(7)

print(my_doubly_linked_list.get(8))

print(my_doubly_linked_list.pop())


my_doubly_linked_list.print_list()


        
    