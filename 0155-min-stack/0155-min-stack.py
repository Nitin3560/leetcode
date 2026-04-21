class MinStack:

    def __init__(self):
        self.stack=[]
        self.m=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.m:
            self.m.append(min(val, self.m[-1]))
        else:
            self.m.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.m.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.m[-1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()