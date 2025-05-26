class Solution(object):
    def canAttendMeetings(self, intervals):
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])

        for i in range(1, len(intervals)):
            if starts[i] < ends[i - 1]:
                return False
        return True