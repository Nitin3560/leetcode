class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = {}
    
        for num in nums:
            if num in count:
                count[num] = count[num] + 1
            else:
                count[num] = 1
        
        operations = 0
        keys = []
        for key in count:
            keys.append(key)
        
        for i in range(len(keys)):
            x = keys[i]
            if x not in count:
                continue
            
            complement = k - x
            
            if complement not in count:
                continue
            
            if x < complement:
                if count[x] < count[complement]:
                    pair_count = count[x]
                else:
                    pair_count = count[complement]
                operations = operations + pair_count
            
            elif x == complement:
                pair_count = count[x] // 2
                operations = operations + pair_count
            
        
        return operations