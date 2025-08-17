class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        ak = float('-inf')
        stack = []

        for x in reversed(nums):
            if x < ak:
                return True
            while stack and stack[-1] < x:
                ak = stack.pop()
            stack.append(x)
        return False