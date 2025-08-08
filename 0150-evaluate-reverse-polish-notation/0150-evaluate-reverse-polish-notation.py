class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for t in tokens:
            if t in {"+", "-", "*", "/"}:
                a = stack.pop()  
                b = stack.pop()  
                if t == "+":
                    stack.append(b + a)
                elif t == "-":
                    stack.append(b - a)
                elif t == "*":
                    stack.append(b * a)
                else: 
                    stack.append(int(b / a))
            else:
                stack.append(int(t))
        return stack[-1]
