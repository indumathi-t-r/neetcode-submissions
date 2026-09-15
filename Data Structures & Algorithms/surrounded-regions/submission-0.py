class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])

        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        def dfs (r,c):
            if r<0 or r>=row or c<0 or c>=col or board[r][c]!="O":
                return
            
            board[r][c] = "S"

            for nr,nc in directions:
                dfs( r+nr, c+nc)
        
        for r in range(row):
            if board[r][0]=="O":
                dfs(r,0)
            if board[r][col-1]=="O":
                dfs(r,col-1)
        
        for c in range(col):
            if board[0][c]=="O":
                dfs(0,c)
            if board[row-1][c]=="O":
                dfs(row-1,c)
            
        for r in range(row):
            for c in range(col):
                if board[r][c]=="O":
                    board[r][c]="X"
                elif board[r][c]=="S":
                    board[r][c]="O"
        

