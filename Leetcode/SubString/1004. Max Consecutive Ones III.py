class Solution:
    def longestOnes(self, nums, k: int) -> int:
        dic = {1:0, 0:0}
        l = 0
        maxLength = 0
        for r, n in enumerate(nums):
            dic[n]+=1
            while dic[0]>k:
                dic[nums[l]]-=1
                l+=1
            maxLength = max(maxLength, r-l+1)
        return maxLength
        