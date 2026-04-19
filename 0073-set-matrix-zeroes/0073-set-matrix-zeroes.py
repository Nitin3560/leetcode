class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows=len(matrix)
        cols=len(matrix[0])
        firstrow=False
        firstcol=False
        j=0
        while j<cols:
            if matrix[0][j]==0:
                firstrow=True
                break
            j+=1
        i=0
        while i<rows:
            if matrix[i][0]==0:
                firstcol=True
                break
            i+=1
        i=1
        while i<rows:
            j=1
            while j<cols:
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
                j+=1
            i+=1
        i=1
        while i<rows:
            j=1
            while j<cols:
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
                j+=1
            i+=1
        if firstrow:
            j=0
            while j<cols:
                matrix[0][j]=0
                j+=1
        if firstcol:
            i=0
            while i<rows:
                matrix[i][0]=0
                i+=1