class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row = len(grid)
        col = len(grid[0])

        q = deque()
        
        for r in range(row):
            for c in range(col):
                if grid[r][c]==0:
                    q.append((r,c))
        
        directions = [[1,0],[-1,0],[0,-1],[0,1]]

        while q:
            i,j = q.popleft()

            for nr,nc in directions:
                nr = i+nr
                nc = j+nc

                if nr<0 or nc<0 or nr>=row or nc>=col or grid[nr][nc]!=2147483647:
                    continue
                
                grid[nr][nc]= grid[i][j]+1
                q.append((nr,nc))



        


        