class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # n = len(citations)
        # for h in range(n,0,-1):
        #     count = 0
        #     for c in citations:
        #         if c >= h:
        #             count += 1
        #     if count >= h:
        #         return h
        # return 0
        citations.sort(reverse=True)
        h = 0
        for i in range(len(citations)):
            if citations[i] >= i+1:
                h = i+1
            else:
                break
        return h