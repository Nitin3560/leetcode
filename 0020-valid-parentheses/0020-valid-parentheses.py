class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stack.append(s[0])
        bracket_map = { ')': '(', ']': '[', '}': '{' }
        for i in range(1,len(s)):
            if stack and s[i] in bracket_map and stack[-1] == bracket_map[s[i]]:
                stack.pop()
            else:
                stack.append(s[i])
                
        return not stack

            
            
        