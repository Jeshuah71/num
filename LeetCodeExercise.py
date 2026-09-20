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


# Two sum exercise 

# Array of integers nums and a integer target return indices of the two numbers such that add up to target 

class Solution(object):
    def two_sums(self, nums, target):
        
        # creation of hash table that is going to store num and index 
        seen = {}
        
        # This is to loop through all index in the array 
        for i, num in enumerate(nums): # Here I am assigning index and value 
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
        # store in the hash table and with the value and the index 
        seen[num] = i 
    
    def sum_two_list(self, l1, l2):
        
        dummy = Node(0)
        
        current = dummy
        
        carry = 0
        
        while l1 or l2 or carry:
            
            val1 = l1.val if l1 else 0
            
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry 
            
            carry = total // 10
            
            digit = total % 10
            
            current.next = Node(digit)
            
            current = current.next 
            
            if l1:
                l1 = l1.next 
                
            if l2 :
                l2 = l2.next
        return dummy.next
    
    def length_of_largest_substring(s):
        
        # stores characters currently inside our window
        chars = set()
        
        # Left seide of the window 
        left = 0
        
        # Best answer so dar
        max_length = 0
        
        for right in range(len(s)):
            chars.remove(s[right])
        
            while s[right] in chars:
                chars.remove(s[left])
                
                left += 1
                
            chars.add(s[right])
            
            window_length = right - left + 1
            
            max_length = max(max_length, window_length)
        return max_length
        
            
    def maxProfit(prices):
        
        # Lowest price we have seen so far 
        min_price = float("inf")
        
        # Best profit we have seen so fare
        max_profit = 0
        
        # Go through every stock price 
    
        for price in prices:
            
            # if this price is cheaper update our best buying price 
            if price < min_price:
                min_price = price
            
            # calculate profit if we sell today
            profit = price - min_price
            
            # keep the best profit 
            max_profit = max(max_profit, profit)
        
        # return the best profit found 
        return max_profit
            
            