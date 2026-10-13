class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)


        if total %2 != 0:
            return False
        
        target = total //2

        def dp(i,remain):

            if remain ==0:
                return True
            
            if remain <0 or i == len(nums):
                return False
            
            return dp (i+1, remain - nums[i]) or dp (i+1, remain)
        
        return dp(0,target)

        