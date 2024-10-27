from typing import List 
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        dic = {0:0, 1:0}
        l = 0 
        maxLength = 0
        for r, n in enumerate(nums):
            dic[n]+=1
            while dic[0]>1:
                dic[nums[l]]-=1
                l+=1
            
            maxLength = max(maxLength, r-l+1)
        return maxLength


nums = [1, 0, 1, 1, 0, 1, 1, 1, 0, 1,1,1]
ob = Solution()
ans = ob.findMaxConsecutiveOnes(nums)
print(ans)