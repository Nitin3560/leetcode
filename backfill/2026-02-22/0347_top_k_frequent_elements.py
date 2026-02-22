class Solution:
    def topKFrequent(self, nums, k):
        from collections import Counter
        return [x for x,_ in Counter(nums).most_common(k)]
