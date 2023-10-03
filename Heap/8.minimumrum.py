from typing import List
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        starts = sorted([interval[0] for interval in intervals])
        ends  = sorted([interval[1] for interval in intervals])
        minroom = 0
        endp = 0
        for start in starts:
            if start<ends[endp]:
                minroom+=1
            else:
                endp+=1
        return minroom
ob = Solution()
intervals = [[0,30],[5,10],[15,20]]
ans = ob.minMeetingRooms(intervals)
print(ans)
