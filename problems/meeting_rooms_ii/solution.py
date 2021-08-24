class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        freeRooms = []
        
        intervals.sort()
        heapq.heappush(freeRooms, intervals[0][1])
        
        for interval in intervals[1:]:
            if( freeRooms[0] <= interval[0] ):
                heapq.heappop(freeRooms)
            heapq.heappush(freeRooms, interval[1])
        return len(freeRooms)
        #Note to myself: Learn heaps and approach 2.
