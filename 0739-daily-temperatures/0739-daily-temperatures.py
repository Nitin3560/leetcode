class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stack = []
        nextwarm = [0] * n
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                nextwarm[stack[-1]] = i - stack[-1] 
                stack.pop()
            stack.append(i)  
        return nextwarm