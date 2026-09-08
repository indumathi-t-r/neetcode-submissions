class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for interval in intervals:
            # checking curr interval before new interval
            if interval[1] < newInterval[0]:
                res.append(interval)
            # checking new interval comes before curr
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                newInterval = interval

            else:
                newInterval[0] = min(interval[0],newInterval[0])
                newInterval[1] = max(interval[1],newInterval[1])       
        res.append(newInterval)

        return res
