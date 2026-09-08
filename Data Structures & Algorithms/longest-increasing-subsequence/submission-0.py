class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                l, r = 0, len(dp) - 1

                while l <= r:
                    mid = (l + r) // 2

                    if dp[mid] < nums[i]:
                        l = mid + 1
                    else:
                        r = mid - 1

                dp[l] = nums[i]

        return len(dp)