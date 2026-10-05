# Hash map 
def two_sum(nums, target):
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i 
    return []


def teo_sums(nums, target):
    seen = {}
    
    for i, num in enumerate(nums):
        
        complement = target - num 
        
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i 
    return [] 



# Two pointers paor in sorted array, plindrome
def is_palindrome(s):
    s = [c.lower() for c in s if c.isalnum()]
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True