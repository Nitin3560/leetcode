class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures) 
        stack = [] 
        stack.append((temperatures[0],0))

        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                prev_temp, prev_index = stack.pop()
                result[prev_index] = i - prev_index  # days waited

            stack.append((temperatures[i], i))

        return result

            
                
            
            