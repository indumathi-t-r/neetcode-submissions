class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum, cursum = nums[0], 0

        for n in nums:
            if cursum<0:
                cursum = 0
            
            cursum+= n
            maxsum = max(maxsum, cursum)
            
        return maxsum