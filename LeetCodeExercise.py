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
            
# leetcode exercise LRU

class LLNode:
    def __init__(self, key, value):
        # Store both key and value
        self.key = key
        self.value = value
        
        # Point for double linked list 
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        # Maximum number of items allowed 
        self.capacity = capacity
        
        #Hash map: 
        # key -> node
        
        self.cache = {}
        
        # Dummy Nodes
        
        self.left = LLNode(0,0)
        self.right = LLNode(0,0)
        
        # Connect dummy Nodes
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        # Get node before and after current node
        prev_node = node.prev
        next_node = node.next 
        
        # Skip current node
        prev_node.next = next_node 
        next_node_prev = prev_node
    
    def insert(self, node):
        # Insert node right before self.right
        # This makes it the Most Recently Used node

        prev_node = self.right.prev

        prev_node.next = node
        node.prev = prev_node

        node.next = self.right
        self.right.prev = node


    def get(self, key):
        # If key does not exist
        if key not in self.cache:
            return -1

        # Get node from hash map
        node = self.cache[key]

        # Move it to MRU position
        self.remove(node)
        self.insert(node)

        # Return its value
        return node.value


    def put(self, key, value):
        # If key already exists,
        # remove the old node from the linked list
        if key in self.cache:
            self.remove(self.cache[key])

        # Create new node
        node = LLNode(key, value)

        # Store key -> node
        self.cache[key] = node

        # Put node in MRU position
        self.insert(node)

        # If we exceed capacity
        if len(self.cache) > self.capacity:

            # The node after left is always the LRU
            lru = self.left.next

            # Remove LRU from linked list
            self.remove(lru)

            # Remove LRU from hash map
            del self.cache[lru.key]

# Leetcode exercise Roman to integer

# The Roman numerals are added VIII = 5 + 1 + 1 + 1 = 8

# If a smaller calue appear before a larger value you substract it

# A python dictionary is perfect 

class Solution:
    def romanToInt(self, s: str) -> int:
        # This is a look up table
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        total = 0
        previous = 0
        
        for char in reversed(s):
            
            current = values[char]
            
            if current < previous:
                total -= current
            else:
                total += current
            previous = current
            
        return total 
    
    # The time complexity is O(n) and the space complexity is O(1)
    
# Longest Common Prefix 

    def longestCommonPrefix(self, strs):
        
        # Loop through each index of the first word
        for i in range(len(strs[0])):
            
            # compare the index with every word 
            for word in strs:
                
                # if the current word is too short, stop 
                if i >= len(word):
                    return strs[0][:i]
                
                # if the characters are different, stop 
                if word[i] != strs[0][i]:
                    return strs[0][:i]
        # if everything matched, return the whole first word 
        return strs[0]
    

# Valid parenthesis 
    def isValid(self, s):
        
        # Stach stores the opening brackets
        stack = []
        
        # Map each closing bracket to its matching opening bracket
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        
        # Go through every character 
        for char in s:
            
            # if it is an opening bracket, and it to the stack
            if char in "([{":
                stack.append(char)
            
            else:
                # if stack is empty, there is nothing to match
                if not stack:
                    return False
                
                # Check if the top opening bracket matches
                if stack[-1] != pairs[char]:
                    return False
                
                # They matched, so remove the openin bracket
                stack.pop()
    # Valid only if every opening bracket was closed
        return len(stack) == 0
    
# Merge two sorted list 
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        dummy = ListNode(0)
        
        current = dummy
        
        while list1 and list2:
            
            if list1.value <= list2.value:
                current.next = list1
                list1 = list1.next
            
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        else:
            current.next = list2
        return dummy.next
    
    def searchInsert(self, nums, target):
        # left and right boundaries of the search area
        left = 0
        right = len(nums) - 1
        
        # keep searching while the area is valid
        while left <= right:
            
            # Find the middle insdex
            mid = (left + right) // 2
            
            # if target is found, return its index
            if nums[mid] == target:
                return mid
            
            # if target is bigger, search the right half
            elif nums[mid] < target:
                left = mid + 1
            
            # if target is smaller, search the left half
            else:
                right = mid - 1 
        # if target was not found 
        # left is the correct insertion position 
        return left
    
    # find a substring 
    
    def lengthOfLastWord(self, s):
        
        # start at the last character
        i = len(s) - 1
        
        # skip spaces at the end
        while i >= 0 and s[i] == " ":
            i -= 1
            
        # start counting the last word
        count = 0
        
        
        while i > 0 and s[i] != " ":
            count += 1
            i -= 1
        return count 
    
    def plusOne(self, digits):
        
        # start at the last digit
        i = len(digits) - 1
        
        # Move from right to left
        while i >= 0:
            
            # if curent digit is less than 9,
            # just add 1 and we are done
            if digits[i] < 9:
                digits[i] += 1
                return digits
        
            # if current digits is 9,
            # make it 0 and carry to the left
            digits[i] = 0
            i -= 1
            
        # if we finished the loop 
        # all digits were 9
        return [1] + digits
    
    def addBinary(self, a,b):
        
        # start at the last digit of each string
        i = len(a)  -1 
        j = len(b) - 1 
        
        # sotres carry from binary addition 
        carry = 0
        
        # Store result digits here
        result = []
        
        # Continuos while there are digits left or a carry
        while i >= 0 or j >= 0 or carry:
            
            # Get current digit from a, or 0 if a is finished 
            digit_a = int(a[i]) if i >= 0 else 0
            
            # get current digit form b, or 0 if b is finished
            digit_b = int(b[j]) if j >= 0 else 0
            
            # Add both digits and the carry
            total = digit_a + digit_b + carry
            
            # Current binary digit 
            result.append(str(total % 2))
            
            # New carry 
            carry = total // 2
            
            # Move both pointers left
            i -= 1
            j -= 1 
        # We built the result backwards
        result.reverse()
        
        # Convert list into a string 
        return "".join(result)
    

    def mySqrt(self, x):
       
       # Search space for the answer
        left = 0
        right = x
       
       # best valid answer found so far
        answer = 0
       
       # Binary Search 
        while left <= right:
           
           # middle possible answer
           mid = (left + right) // 2
           
           # Square of the middle number
           square = mid * mid
           
           # Exact square root found 
           if square == x:
               return mid 
           
           # mid is too small, but still a valid candidate
           elif square < x:
               answer = mid
               left = mid + 1
               
            # mid is too large 
           else: 
               right = mid - 1 
               
        return answer  