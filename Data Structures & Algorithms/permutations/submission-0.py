class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path =[]
        used = set()

        def dfs():
            if len(path)==len(nums):
                res.append(path.copy())
                return
            for i in nums:
                if i in used:
                    continue
                path.append(i)
                used.add(i)
                dfs()
                path.pop()
                used.remove(i)
        dfs()
        return res
                

        