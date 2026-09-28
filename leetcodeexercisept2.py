class ListNode(object):
    def __init__()

# two sums exercise here we need to know the pattern but also see what are we trying to look for 
def two_sums(self, nums, target):
    
    seen = {}
    
    for i, num in enumerate(nums):
        
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
        
# add two numbers

    def addTwoNumbers(self, l1, l2):
        
        dummy = Node