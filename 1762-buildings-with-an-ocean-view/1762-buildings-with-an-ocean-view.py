class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n =len(heights)
        stack =[]
        nextGreater =[-1] * n
        for i in range(n):
            while stack and heights[stack[-1]] <= heights[i]: 
                nextGreater[stack[-1]] = i
                stack.pop()
            stack.append(i)
        return [i for i in range(n) if nextGreater[i] == -1]