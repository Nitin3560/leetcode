class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # res=[]
        # def backtrack(start,path):
        #     res.append(path[:])
        #     for i in range(start,len(nums)):
        #         path.append(nums[i])
        #         backtrack(i+1,path)
        #         path.pop()
        # backtrack(0,[])
        # return res
        result = []
    
        def backtrack(start: int, current: list[int]):
            result.append(current[:])
            
            for i in range(start, len(nums)):
                current.append(nums[i]) 
                backtrack(i + 1, current)
                current.pop()
        
        backtrack(0, [])
        return result