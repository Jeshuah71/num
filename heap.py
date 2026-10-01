class MaxHeap: 
    def __init__(self):
        self.heap = []
    
    def _left_child(self, index):
        return 2 * index + 1 
    
    def _right_child(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index - 1) // 2
    
    def _swap(self, index1, index2):
        self.head[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        
    # inser tin heap 
        
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1
        
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)
            
        
    # remove in a heap 
    def remove(self):
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        
        return max_value
    
    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)
            
            if (left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]):
                max_index = left_index
                
            if (right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]):
                max_index = right_index
                
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
    # inser of min head 
    def insert(self, value):
        # add the new value at the end of the heap
        self.heap.append(value)
        
        # index of the new value 
        current = len(self.heap) - 1 
        
        # keep moving up while it is smaller than its parent 
        while current > 0:
            parent = self._parent(current)
            
            # if current value is smaller than parent, swap them 
            if self.head[current] < self.heap[parent]:
                self._swap(current, parent)
                
                # move current index up 
                current = parent 
            else:
                # Heap property is correct 
                break 
    # sink down 
    def remove(self):
        # if the heap is empty, there is nothing to remove
        if len(self.heap) == 0:
            return None
        
        # If there is only one value, remove it and return it
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # Save the minimum value that is the root in this case of min head
        min_value = self.heap[0]
        
        # Take the last value and move it to the root 
        self.heap[0] = self.heap.pop()
        
        
        # Move the new root down until 
        # the Min Heap property is restored
        self._sink_down(0)
        
        # Return the original minimum. value 
        return min_value
    # def sink down in min head
    def _sink_down(self, index):
        # Assume the current node is the smallest 
        min_index = index 
        
        # Keep trying to move the value down
        while True:
            
            # Get child indexes 
            left_index = self._left_child(index)
            right_index = self._right_child(index)
            
            # if left child exists and is smaller than current smallest, update min_index
            if (left_index < len(self.heap) and self.heap[left_index] < self.heap[min_index]):
                min_index = left_index
                
            # if right child exists and is smaller than current smallest, update min)index
            if (right_index < len(self.heap) and self.heap[right_index] < self.heap[min_index]):
                min_index = right_index
                
            # if index is still the smallest, the heap is correct 
            if min_index == index:
                break
            
            # Otherwise swap with the smaller child 
            self._swap(index, min_index)
            
            # Continue form the new position 
            index = min_index
            
# find the kth smalles in the Max heap
def find_kth_smallest(nums, k):
    # Create an empty Max Heap
    max_heap = MaxHeap()
        
    # Go through every number
    for num in nums:
            
        # Add the number to the heap
        max_heap.insert(num)
            
        # We only want to keep k numbers in the heap
        # If we have more than k, remove the largest
        if len(max_heap.heap) > k:
            max_heap.remove()
                
    # The root is the kth smallest number
    return max_heap.heap[0]

def stream_max(nums):
    # Create an empty Max Heap 
    max_heap = MaxHeap()
    
    # Store the maximum seen after each number 
    result = []
    
    # Go through every number 
    for num in nums:
        
        # Add current number to the heap
        max_heap.insert(num)
        
        
        # In a Max Heap, index 0 is always the largest
        current_max = max_heap.heap[0]
        
        # Add the current maximum to the result 
        result.append(current_max)
    return result
    
    
# find pairs 
def find_pairs(arr1, arr2, target):
    # Convert arr1 to a set for a fast lookup
    set1 = set(arr1)
        
    # Store all valid pairs 
    pairs = []
        
    # Go through arr2 in order
    for num in arr2:
            
        # Find the number we need form arr1 
        needed = target - num 
            
        # if that number exists in arr1, 
        # we found a valid pair 
        if needed in set1: 
            pairs.append((needed, sum))
                
    return pairs
    
# longest consecutive sequence in sets
def lingest_consecutive_sequence(nums):
    # put all numbers into a set for fast lookup 
    num_set = set(nums)
        
    # Store the lingest sequence length found
    longest = 0
        
        # Go through every unique number
    for num in num_set:
            
        # If num -1 doesn't exist
        # then num is the beginning of a sequence
        if num - 1 not in num_set:
                
            # Start the sequence at num 
            current_num = num 
                
            # Current sequence has at least 1 number 
            current_length = 1 
                
            # keep looking for the next consecutive number 
            while current_num + 1 in num_set:
                current_num += 1 
                current_length += 1 
                    
            # Save the lingest seqeunce found 
            longest = max(longest, current_length)
    
    return longest
        