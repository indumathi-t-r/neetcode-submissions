class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = {}

        for source, dest in tickets:
            if source not in graph:
                graph[source] = []
            
            heapq.heappush(graph[source],dest)
        
        res = []
        
        def dfs(airport):

            while airport in graph and graph[airport]:
                cur_port = heapq.heappop(graph[airport])
                dfs(cur_port)
            res.append(airport)
        
        dfs("JFK")

        return res[::-1]

        