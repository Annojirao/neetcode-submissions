"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
        intervals.sort(key=lambda i: i.start)
        initial_meeting = intervals[0]
        for i in range(1,len(intervals)):
            current_meeting = intervals[i]
            if current_meeting.start < initial_meeting.end:
                return False
            else:
                initial_meeting = current_meeting
        return True
