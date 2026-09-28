class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Linkedlist:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1 
        
    def print(self):
        temp = self.head
        
        while temp is not None:
            print(temp.value)
            temp = temp.next 
        
    def append(self, value):
        new_node = Node(0)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length + 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.head 
        pre = self.head 
        while (temp.next):
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
    
    def get(self, index):
        if index < 0 or index >= 0:
            return None
        
        temp = self.head
        
        for _ in range(index):
            temp = temp.next
        return temp
    
    
    def set(self, index, value):
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
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index > self.length:
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
            
    # find middle node in a linked list 
    # we have to crceate two variables fast and slow 
    # while loop to iterate through th elist
    def find_middle_node(self):
        fast = self.head
        slow = self.head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    # has a loop solution 
    # here we also ned a fast and a slow variable 
    # we need a while loop to iterate through the list 
    # then move the list 
    # if fast = slow we return true 
    
    def has_loo(self):
        fast = self.head
        slow = self.head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False
    
    # find kth without the legth has to follow this patter
    # so we have to use two pointers
    # we have to move fast k steps ahead 
    # move slow + fast together 
    # when fast ends slow is the answer
    
    def find_kth(ll, k):
        slow = ll.head
        fast = ll.head
        
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
            
        while fast:
            slow = slow.next
            fast = fast.next
        return slow
    
    # Conversion binary to decimal
    def binary_to_decimal(self):
        # Start at the fisrt node
        current = self.head
        
        
        # this will store the decimal answer
        decimal = 0
        
        # go through every node of the linked list 
        while current: 
            # take the decimal value we already have
            # multiply it by 2
            # then add the current binary digit (0 or 1 )
            
            decimal = decimal * 2 + current.value
            
            # move to the next node
            
            current = current.next
            
        # return the final decimal number
        return decimal
    
    # partition list in linked lists
    def partition_list(self, x):
        
        # if the list is empty, do nothing 
        if self.head is None:
            return
        
        # Dummy node for the values < x
        dummy1 = Node(0)
        
        # dummy node for the value >= x
        dummy2 = Node(0)
        
        # pointer to the end of the < x list
        prev1 = dummy1
        
        # pointer to the end of the >= x list
        prev2 = dummy2
        
        # start at the head of the original list
        current = self.head
        
        # Go through every node
        
        while current:
            
            # if current value is less than x
            if current.value < x:
                
                # Add the current node to the list that is for the values less tham
                prev1.next = current
                
                # move the prev1 forward
                prev1 = current
                
            else:
                # add current node to the second list
                prev2.next = current
                
                # move the prev2 forward 
            
            # move to the next original node to keep[ comparing
            current = current.next
        
        # end the second list
        prev2.next = None
        
        # connect first list with second list
        
        prev1.next = dummy2.next
        
        # POINT dummy node ot head 
        self.head = dummy1.next
        
    def swap_pairs(self):
        
        # Create a fake node before the head
        dummy = Node(0)
        
        # Dummy points to the original head
        dummy.next = self.head
        
        # Prev starts at the dummy node
        prev = dummy
        
        # continue while these are two nodes available to swap
        while prev.next and prev.next.next:
            
            # first nde of the pair
            first = prev.next
            
            # second node of the pait
            second = first.next
            
            # first skips second and points to the node after second
            first.next = second.next
            
            # second now points back to first 
            second.next = first
            
            # previous part of list now points to second
            prev.next = second
            
            # move prev to the end of the swapped pair
            prev = first
        
        # skip the fake dummy node 
        # and make the real first node the new head
        
        self.head = dummy.next
        
    def reverse_between(self, start_index, end_index):
        # if the list is empty, there is nothing to reserve
        if self.head is None:
            return
        
        # if start and end are the same
        # we are reversing only one node
        if start_index == end_index:
            return
        
        # Create a fake node before the head
        dummy = Node(0)
        dummy.next = self.head
        
        # prev will move to the node BEFORE start_index
        prev = dummy
        
        # Mode prev to the correct position 
        for _ in range(start_index):
            prev = prev.next
            
        # current is the first node we want to reverse
        current = prev.next
        
        # Reverse the section 
        for _ in range(end_index - start_index):
            temp = current.next 
            
            current.next = temp.next 
            
            temp.next = prev.next 
            
            prev.next = temp
        # update head in case start index was 0 
        self.head = dummy.next
        
        
    
            
