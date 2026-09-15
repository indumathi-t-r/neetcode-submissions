class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph =[[] for _ in range(numCourses)]

        indegree = [0] * numCourses

        for course,preq in prerequisites:
            graph[preq].append(course)

            indegree[course]+=1
        
        q = deque()

        for c in range(numCourses):
            if indegree[c]==0:
                q.append(c)
            
        ans = []

        while q:
            cur = q.popleft()
            ans.append(cur)

            for nei in graph[cur]:
                indegree[nei] -=1
                if indegree[nei]==0:
                    q.append(nei)
        
        if len(ans)==numCourses:
            return ans
        return []
        