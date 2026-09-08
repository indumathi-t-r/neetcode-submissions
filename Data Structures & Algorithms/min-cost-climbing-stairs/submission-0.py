class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev2 = cost[0]
        prev1 = cost[1]
        

        for i in range(2,n):
            cur = cost[i] + min(prev2,prev1)
            prev2 = prev1
            prev1 = cur
        
        return min(prev1,prev2)
        