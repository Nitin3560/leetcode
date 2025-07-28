class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        arr=sorted(heights)
        count=0
        for i,j in zip(heights,arr):
            if i!=j:
                count+=1
                
        return count