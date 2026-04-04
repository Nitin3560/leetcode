class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        set={}
        for num in nums:
            if num in set:
                set[num]+=1
            else:
                set[num]=1
        max_freq=0
        max_num=0
        for num in set:
            if set[num]>max_freq:
                max_freq=set[num]
                max_num=num
        return max_num