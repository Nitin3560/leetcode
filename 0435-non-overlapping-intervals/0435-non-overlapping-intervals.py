class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        remove = 0
        curr = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, len(intervals)):
           
            if intervals[i][0] >= end:
                curr = intervals[i][0]
                end = intervals[i][1]
            else:
                remove += 1
                end = min(end, intervals[i][1])

        return remove