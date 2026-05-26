"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        t = []
        for i in intervals:
            t.append((i.start,1))
            t.append((i.end, -1))
        t.sort()
        ans = 0
        cur = 0
        for _, v in t:
            cur += v
            ans = max(ans, cur)
        return ans
