class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []

        curr = intervals[0]
        for i in range(1,len(intervals)):

            if intervals[i][0]<=curr[1]:
                curr[1] = max(intervals[i][1],curr[1])
            
            else:
                ans.append(curr)

                curr = intervals[i]
        ans.append(curr)
        return ans