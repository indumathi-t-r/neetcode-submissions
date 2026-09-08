class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_ar = 0

        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        n = len(grid)
        m = len(grid[0])

        def dfs(r,c):
            if (r<0 or c<0 or r>=n or c>=m or grid[r][c]==0):
                return 0
            

            grid[r][c] = 0
            ar = 1
            for nr,nc in directions:
                ar += dfs( r+nr , c+nc)

            return ar

            
        for r in range(n):
            for c in range(m):
                if grid[r][c]==1:
                    max_ar = max(max_ar,dfs(r,c))

        return max_ar
                    

                

        