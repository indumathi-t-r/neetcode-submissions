class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = set()

        def dfs(start,cur):
            res.append(cur.copy())
            for j in range(start,len(nums)):
                if j>start and nums[j] == nums[j-1]:
                    continue
                cur.append(nums[j])
                dfs(j+1,cur)
                cur.pop()
        dfs(0,[])
        return res
            
            
        