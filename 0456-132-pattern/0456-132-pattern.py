class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n =len(nums)
        minnum =[float('inf')] * n
        for i in range(1,n):
            minnum[i] = min(minnum[i-1],nums[i-1])
        stack =[]
        for k in range(n):
            while stack and nums[stack[-1]] <=nums[k]:
                stack.pop()
            if stack:
                j =stack[-1]           
                if minnum[j] <nums[k]:
                    return True
            stack.append(k) 
        return False