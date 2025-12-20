class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n=len(s)
        a=[n]*n
        p=-n
        for i in range(n):
            if s[i]==c:p=i
            a[i]=i-p
        p=2*n
        for i in range(n-1,-1,-1):
            if s[i]==c:p=i
            a[i]=min(a[i],p-i)
        return a







