class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = [[] for _ in range(n+1)]
        ans = 0

        for u,v, wei in times:
            graph[u].append((v,wei))
        
        dist = [float("inf")] * (n+1)
        dist[k] = 0

        min_heap = [(0,k)]

        while min_heap:

            cur_time , node = heapq.heappop(min_heap)
            if cur_time > dist[node]:
                continue

            for nei, wei in graph[node]:
                if cur_time + wei < dist[nei]:
                    dist[nei] = cur_time + wei
                    heapq.heappush(min_heap,(cur_time+wei , nei))
        
        ans = max(dist[1:])

        if ans == float("inf"):
            return -1
        
        return ans

                
        