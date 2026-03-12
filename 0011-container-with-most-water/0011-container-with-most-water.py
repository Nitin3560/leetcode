class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water=0
        l=0
        r=len(height)-1
        while l < r:
            if height[l]< height[r]:
                water = (r-l)* min(height[l], height[r])
                l+=1
            elif height[l]==height[r]:
                water= (r-l)* min (height[l], height[r])
                r-=1
                l+=1
            else:
                water= (r-l)* min (height[l], height[r])
                r-=1
            max_water=max(max_water, water)
        return max_water

