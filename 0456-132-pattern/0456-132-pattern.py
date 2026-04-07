class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        num =float('-inf')
        stack =[]
        for x in reversed(nums):
            if x <num:
                return True
            while stack and stack[-1] < x:
                num =stack.pop()
            stack.append(x)
        return False