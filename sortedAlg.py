# Bubble sort
def bubble_sort(my_list):
    for i in range(len(my_list) -1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
    return my_list


# selection sort 
def selection_sort(my_list):
    for i in range(len(my_list)-1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if min_index != i:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j > - 1:
            my_list[j + 1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list

# Merge function 

def merge(list1, list2):
    combined = []
    
    i = 0 
    j = 0 
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
            
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    
    while j < len(list2):
        combined.append(list2[j])
        j += 1
        
    return combined 

def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list) / 2)
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])
    
    return merge(left, right)

# Quick sort
def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp
    
def pivot(mylist, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if mylist[i] < mylist[pivot_index]:
            swap_index += 1
            swap(mylist, swap_index, i)
    swap(mylist, pivot_index, swap_index)
    return swap_index

def quick_sort_helper(my_list, left, right):
    pivot_index = pivot(my_list, left, right)
    
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index - 1)
        quick_sort_helper(my_list, pivot_index + 1, right)
    return my_list

def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list) - 1)

# Def bubble sort in a LL 

def bubble_sort(self):
    # Empty list or one node is already sorted 
    if self.length < 2:
        return 
    
    # Sorted until marks the beggining of the already sorted section at the end
    sorted_until = None
    
    while sorted_until != self.head:
        current = self.head
        swapped = False
        # OCmpare adjecent nodes
        while current.next != sorted_until:
            if current.value > current.next.value:
                # Swap values 
                current.value, current.next.value = current.next.value, current.value
                swapped = True
            current = current.next
        # current is now the last node 
        # in the unsorted section 
        sorted_until = current
        
        # if not swaps happened, list is already sorted 
        if not swapped:
            break
        
        
# Selection sort in a LL
def selection_sort(self):
    # empty list or one node is already sorted
    if self.length < 2:
        return
    
    current = self.head
    
    while current:
        smallest = current
        temp = current.next
        
        # Find the smallest value in the remaining list
        while temp:
            if temp.value < smallest.value:
                smallest = temp
            temp = temp.next
            
        # Swap the values
        if smallest != current:
            current.value, smallest.value = smallest.value, current.value
        
        # move to the next position 
        current = current.next
        
def insertion_sort(self):
    # empty list or one node is already sorted
    if self.length < 2:
        return
    
    # The first node starts the sorted section
    sorted_head =  self.head
    
    # Current starts at the second node 
    current = self.head.next
    
    # Disconnect the sorted section from the unsorted section
    sorted_head.next = None
    
    while current:
        # Save the next unsorted node
        next_node = current.next
        
        # Case 1 current belong at the front 
        if current.value < sorted_head.value:
            current.next = sorted_head
            sorted_head = current
            
        else:
            # Case 2 current belongs somewhere after the front 
            search = sorted_head
            while search.next and search.next.value < current.value:
                search = search.next
            
            # Insert current after search
            current.next = search.next
            search.next = current
        # Move to the next unsorted node
        current = next_node
        
    self.head = sorted_head
    
    # update tail 
    self.tail = self.head
    while self.tail.next:
        self.tail = self.tail.next