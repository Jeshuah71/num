class HashTable:
    
    def __init__(self):
        self.data_map = [None] * size 
        
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
            
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index] [i][0] == key:
                    return self.data_map[index] [i] [1]
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            for j in range(len(self.data_map[i])):
                all_keys.append(self.data_map[i][j][0])
        return all_keys
    
    # leetcode exercide item in common in two lists 
    def item_in_common(list1, list2):
        my_dict = {}
        
        for i in list1:
            my_dict[i] = True
        for j in list2:
            if j in my_dict:
                return True
        
        return False 

    def find_duplicates(nums):
        
        # Dictionary to count how many times each number appears
        counts = {}
        
        # list where we will store the duplicate numbers
        duplicates = []
        
        # Go through every number in the input list 
        for num in nums:
            
            # if we have seen this number before,
            # increase its count by 1
            if num in counts:
                counts[num] += 1 
            
            # if this is the first time we see the number
            # add it to the dictionary with count 1
            
            else:
                counts[num] = 1
        
        # Now we go through the dictionary
        for num in counts:
            
            # if a number appeared more than once
            # it is a duplicate
            if counts[num] > 1:
                duplicates.append(num)
        # Return all duplicate numbers
        return duplicates
    
    def first_non_repeating_char(string):
        # Dictionary to count how many times each character appears
        counts = {}
        
        # Fisrt loop: count every character
        for char in string:
            
            # If we have seen this character before, increase its count
            if char in counts:
                counts[char] += 1
            
            # if this is the first time we see it, start its count at 1 
            else:
                counts[char] = 1
                
        # Second loop: go through the sting in original order
        for char in string:
            
            # if this character appears only once, it is the first non-repeating character
            if counts[char] == 1:
                return char
        
        return  None

    def group_anagrams(strings):
        
        # Dictionary to store groups of anagram
        anagrams = {}
        
        # Go through each word
        for word in strings:
            
            # sort the letter in the word
            # Example: "tea" -> "aet"
            key = "".join(sorted(word))
            
            # if this sorted version is not yet in the dictionary,
            # create a new empty list for it 
            if key not in anagrams:
                anagrams[key] = []
                
            
            # add the original word to its group 
            anagrams[key].append(word)
            
        # Return only the groups 
        return list(anagrams.values())
                
    # Two sums
    def two_sum(nums, target):
        
        # Dictionary:
        # number -> index where we saw that number
        seen = {}
        
        # Go through the array only once
        for i, num in enumerate(nums):
            
            # Find the number we need to reach the target 
            needed = target - num
            
            # if we already saw that number, we found the answer
            if needed in seen:
                return [seen[needed], i]
            
            
            # Otherweise remember the current number and its index 
            seen[num] = i 
        
        # if no pair adds up to target
        return []
    
    
    def subarray_sum(nums, target):
        
        # Dictionary: prefix sum -> index where we saw that sum
        sums = {0: -1}
        
        # Running total 
        current_sum = 0
        
        # Go through the array once
        for i, num in enumerate(nums):
            
            # add current number to running sum
            current_sum += num
            
            # what previous sum do we need?
            needed = current_sum - target
            
            # we saw that sum before, the numbers after index up to i , add up to target
            if needed in sums:
                return [sums[needed] + 1, i]

            # Remember this running sum and its index
            sums[current_sum] = i
        
        # No matching subarray found
        return []
    
    # set introduction
    # set remove duplicates
    def remove_duplicates(my_list):
        # Convert the list to a set
        # A set removes duplicates values automatically
        unique_values = set(my_list)
        
        # convert the set back to a list
        return list(unique_values)
    
    def has_unique_chars(string):
        # Set to store characters we have already seen
        seen = set()
        
        # Go through each character in the string 
        for char in string:
            
            # if the character is already in the set, then it is a duplicate
            if char in seen:
                return False
        
            # Otherwise, remember this character
            seen.add(char)
        return True
    
    def subarray_sum(nums, target):
        
        # Dictionary:
        # prefix_sum --> index where we saw that sum
        prefix_sums = {0: -1}
        
        # Running total
        current_sum = 0
        
        # Go through the array once
        for i, num in enumerate(nums):
            
            # Add current number to running total
            current_sum += num
            
            # Find what previous sum we need
            needed = current_sum - target
            
            # if we have seen that sum before, 
            # the numbers after that index up to i add to target 
            if needed in prefix_sums:
                return [prefix_sums[needed] + 1, i]
            
            # Save current running sum and its index 
            prefix_sums[current_sum] = i 
        
        # No matching subarray
        return [] 
    
    
my_hash_table = HashTable()

my_hash_table.print_table()


