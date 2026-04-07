class Solution:
    def trap(self, height: List[int]) -> int:
        stack =[]
        water =0
        for i in range(len(height)):
            while stack and height[stack[-1]] <= height[i]:
                stackTop =stack.pop()     
                if not stack:
                    break                         
                j =stack[-1]                   
                width =i -j -1
                bounded_height= min(height[i], height[j])- height[stackTop]
                water +=width *bounded_height
            stack.append(i)
        return water
