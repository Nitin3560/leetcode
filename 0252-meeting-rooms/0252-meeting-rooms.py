class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        n =len(intervals)
        for i in range(n):
            s1, e1 =intervals[i]
            for j in range(i + 1, n):
                s2, e2 =intervals[j]
                if max(s1, s2) < min(e1, e2):
                    return False
        return True