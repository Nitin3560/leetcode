class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxwater=0
        while l<r:
            if height[l]<height[r]:
                water=(r - l) * min(height[l], height[r])
                l+=1
            elif height[l]==height[r]:
                water=(r - l) * min(height[l], height[r])
                l+=1
                r-=1
            else:
                water=(r - l) * min(height[l], height[r])
                r-=1
            maxwater=max(maxwater,water) 

        return maxwater   