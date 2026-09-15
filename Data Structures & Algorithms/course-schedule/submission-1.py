class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = [[] for _ in range(numCourses)]

        indegree = [0]* numCourses

        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u] +=1
        
        q = deque()

        for course in range(numCourses):
            if indegree[course]==0:
                q.append(course)
        
        complete = 0
        while q:
            course = q.popleft()
            complete +=1

            for nei in graph[course]:
                indegree[nei] -=1
                
                if indegree[nei]==0:
                    q.append(nei)
            
        return complete == numCourses
                    

        