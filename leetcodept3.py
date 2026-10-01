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