class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        # Transpose then Take row reverse

        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                #swapping row as columns - Transpose
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            
        
        for row in matrix:
            row.reverse()


