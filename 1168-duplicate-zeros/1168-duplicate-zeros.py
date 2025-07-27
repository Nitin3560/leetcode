class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zero=0
        n = len(arr)
        for i in range(len(arr)):
            if arr[i]==0:
                zero+=1
        
        i = n -1
        j = n + zero - 1
        while i >= 0:
            if j<n:
                arr[j]=arr[i]
            if arr[i]==0:
                j-=1
                if j < n:
                    arr[j] = 0
                
            i-=1
            j-=1
            
            