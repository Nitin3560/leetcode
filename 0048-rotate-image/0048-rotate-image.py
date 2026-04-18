class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        for i in range(n//2+n%2):
            for j in range(n//2):
                (matrix[i][j], matrix[j][n-1-i], 
                matrix[n-1-i][n-j-1], matrix[n-1-j][i]) = (matrix[n-1-j][i],  matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-j-1])
            