class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<=2:
            return False
        n=len(arr)
        i=0
        j=n-1
        while i<=j-1:
            if arr[i]<arr[i+1]:
                i+=1
            elif arr[j]<arr[j-1]:
                j-=1
            else:
                break
        if i==j and (j!=n-1 and i!=0):
            return True
        else:
            return False