class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sum = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in sum:
                return [sum[diff] , i]
            sum[n] = i