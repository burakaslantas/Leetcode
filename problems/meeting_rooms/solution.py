class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        
        for i in range(1, len(intervals)):
            firstInterval = intervals[i-1]
            secondInterval = intervals[i]
            if( (firstInterval[1] > secondInterval[0]) ):
                return False
        return True
