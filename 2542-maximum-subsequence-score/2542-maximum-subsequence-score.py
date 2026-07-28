class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        pairs = sorted(zip(nums1, nums2), key=lambda x: -x[1])
        
        min_heap = [] 
        currsum = 0
        result = 0
        
        for val1, val2 in pairs:
            heapq.heappush(min_heap, val1)
            currsum += val1
            
            if len(min_heap) > k:
                smallest = heapq.heappop(min_heap)
                currsum -= smallest
            
            if len(min_heap) == k:
                result = max(result, currsum * val2)
        
        return result