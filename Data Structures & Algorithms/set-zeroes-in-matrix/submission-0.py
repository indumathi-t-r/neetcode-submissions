class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        firstrowzero = False
        firstcolzero = False

        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(cols):
            if matrix[0][i] == 0:
                firstrowzero = True
        
        for j in range(rows):
            if matrix[j][0] == 0:
                firstcolzero = True
        
        for i in range(1, rows):
            for j in range(1,cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, rows):
            for j in range(1,cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if firstrowzero:
            for r in range(cols):
                matrix[0][r] = 0
        if firstcolzero :
            for r in range(rows):
                matrix[r][0] = 0
                
        