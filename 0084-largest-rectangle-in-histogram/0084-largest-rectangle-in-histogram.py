class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        nextSmaller = [n] * n     
        prevSmaller = [-1] * n    

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stackTop = stack.pop()
                nextSmaller[stackTop] = i      
            
            if stack:
                prevSmaller[i] = stack[-1]       

            stack.append(i)

        max_area = 0
        for i in range(n):
            width = nextSmaller[i] - prevSmaller[i] - 1
            area = heights[i] * width
            max_area = max(max_area, area)

        return max_area
