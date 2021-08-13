class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        if len(intervals) <= 1:
            return intervals
        i = 1
        while i < len(intervals):
            if intervals[i-1][1] >= intervals[i][0]:
                intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
                intervals.remove(intervals[i])
            else:
                i += 1
        """for i in range(1, len(intervals)-1):
        IMPORTANT => WHILE ITERATING A LIST, YOU SHOULD NOT REMOVE AN ELEMENT FROM LIST
            print(i)
            if intervals[i-1][1] >= intervals[i][0]:
                intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
                intervals.remove(intervals[i])"""
        return intervals