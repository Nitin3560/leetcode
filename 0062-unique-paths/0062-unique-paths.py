class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        r=m-1;c=n-1
        if r<c:r,c=c,r
        res=1
        for i in range(1,c+1):
            res=res*(r+i)//i
        return res
