class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        
        rows = len(strs)
        cols = len(strs[0])
        
        # ordered[i] tells us whether:
        # strs[i] < strs[i + 1]
        # has already been decided by an earlier kept column
        ordered = [False] * (rows - 1) 
        
        deletions = 0 
        
        # Check columns from left to right 
        for col in range(cols):
            
            # First check whether keeping this column would break any pair that is not already ordered
            bad_column = False
            
            for row in range(rows - 1):
                if not ordered[row]:
                    if strs[row][col] > strs[row + 1][col]:
                        bad_column = True
                        break
                    
            # if this column creates a wrong ordering, delete it and do NOT use it to update anything 
            if bad_column:
                deletions += 1
                continue
            
            # The column is safe to keep. See if it permanently establishes order for any neighboring pair
            for row in range(rows -1):
                if not ordered[row]:
                    if strs[row][col] < strs[row + 1][col]:
                        ordered[row] = True
                        
            # if every neighboring pair is already ordered, later columns can no longer hurt us
            if all(ordered):
                break
        return deletions
    
    
    # Tallest bill board porblem 
    def tallestBillboard(rods):
        # dp[difference] = largest left supporrt height 
        # we can create with that difference
        dp = {0: 0}
        
        # Look at every rod
        for rod in rods:
            
            # Make a copy because we don't want to modify the states we are currently looping through 
            current = dp.copy()
            
            # Look at every situtation we have created so far
            for difference, left_height in current.items():
                
                # OPTION 1:
                # put rod pn the LEFT suppport
                new_difference = difference + rod
                new_left_height = left_height + rod
                
                dp[new_difference] = max(dp.get(new_difference, -1), new_left_height)
                
                # OPTION 2:
                # Put rod on the RIGHT support
                new_difference = difference - rod
                
                # left height does not change 
                dp[new_difference] = max(dp.get(new_difference, -1), left_height)
                
                # OPTION 3 
                # don't use the rod 
                # This is already handled because dp keeps old values 
        # Difference 0 means both supports have equal height 
        return dp[0]
    
    # Max consecutive ones 
    
    def findMaxConsecutiveOnes(nums):
        # Count of consecutive 1s we are currently seeing
        current_count = 0
        
        # Longest consecutive sequence of 1s found so far 
        max_count = 0
        
        # Look at every number
        for num in nums:
            
            # If we see a 1, continue the streak
            if num == 1:
                current_count += 1
                
                # Save the largest strack we have seen
                max_count = max(max_count, current_count)
                
            # if we see a 0, the streak ends
            else:
                current_count = 0
        # Return the longest streak
        return max_count
    
    # Concatenation of arrays
    def getConcatenation(self,nums):
        
        ans = [] 
        
        # Add every number of nums
        for num in nums:
            ans.append(num)
        
        # Add every number for nums again
        for num in nums:
            ans.append(num)
        return ans
    
    # Contiguous Array
    def findMaxLength(self, nums):
        # Stores the first index where each prefix sum appeared
        first_seen = {0: -1}
        
        prefix_sum = 0
        max_length = 0
        
        for i, num in enumerate(nums):
            
            # Treat 0 as -1 and 1 as + 1
            if num == 0:
                prefix_sum -=1
            else:
                prefix_sum += 1
                
            # If we have seen this prefix 
            # The elements between those two positions sum to 0
            if prefix_sum in first_seen:
                length = i - first_seen[prefix_sum]
                max_length = max(max_length, length)
            
            else:
                # only save the FIRST time we see this prefix sum
                # because that gives us the longest possible subarray later
                first_seen[prefix_sum] = i
        return max_length
    
    def canMakeSameParity(self, nums1):
        smallest = min(nums1)
        
        # If the smalles number is odd,
        # Every even number can substract it and become odd
        if smallest % 2 == 1:
            return True
        
        # if the smallest number is even, 
        # the only way this works is if EVERY number is even
        for num in nums1:
            if num % 2 == 1:
                return False
            
        return True
    
    # Def divide
    
    def divide(self, dividend: int, divisor: int) -> int:
        # 32-bit integer limits 
        INT_MAX = 2**31 -1
        INT_MIN = -2**31
        
        # Special overflow case:
        # -2147483648 / -1 = 2147483648
        # which is larger than INT_MAX
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Result is negative if exactly one number is negative
        negative = (dividend < 0) != (divisor <0)
        
        # Work with positive values
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        
        # keep subtracting until dividend is smaller than divisor
        while dividend >= divisor:
            current_divisor = divisor
            multiple = 1
            
            # Double current_divisor until doubling again
            # Would make it larger than divided
            while dividend >= (current_divisor << 1):
                current_divisor <<= 1 
                multiple <<= 1 
                
            # Substract the largest chunk we found
            dividend -= current_divisor
            
            # add how many divisors that chunk represents
            quotient += multiple 
            
        # Apply the corrct sign 
        if negative:
            quotient = -quotient 
            
        return quotient 
    
    # strign to integer 
    
    def myAtoi(sefl, s: str) -> int:
        i = 0
        n = len(s)
        
        # 32 bit signed integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Step 1: Skip leading spaces
        while i < n and s[i] == " ":
            i += 1 
            
        # Step 2: Determine the sign 
        sign = 1
        
        if 1 < n and s[i] == "-":
            sign =-1
            i += 1 
        
        elif i < n and s[i] == "+":
            i += 1 
            
        # Step 3: build the number manually 
        number = 0 
        
        while i < n and "0" <= s[i] <= "9": 
            digit = ord(s[i]) - ord("0")
            
            number = number * 10 + digit 
            
            # Check overflow
            if sign * number > INT_MAX:
                return INT_MAX

            if sign * number < INT_MIN:
                return INT_MIN
            
            i += 1 

        # Step 4: apply the sign 
        return sign * number 
    
    
# Database question 
# Select product_id
# FROM Products
# WHERE low_fats = 'Y'
#   AND recyclable = 'Y';

            
        
        