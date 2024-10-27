class Solution:
    def longestSubarray(self, nums) -> int:
        dic = {0:0, 1:1}
        maxLength = 0 
        l = 0
        for r,n in enumerate(nums):
            dic[n]+=1 
            while dic[0]>1:
                dic[nums[l]]-=1 
                l+=1 
            maxLength = max(maxLength, r-l+1-1)
        return maxLength