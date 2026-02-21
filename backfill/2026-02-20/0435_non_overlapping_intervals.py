class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])
        end = None
        keep = 0
        for s, e in intervals:
            if end is None or s >= end:
                keep += 1
                end = e
        return len(intervals) - keep
