class Solution:
    def findKthLargest(self, nums, k):
        import heapq
        minHeap = nums[:k]
        heapq.heapify(minHeap)
        for n in nums[k:]:
            if n > minHeap[0]:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, n)
        return minHeap[0]
if __name__ == '__main__':
    nums = [3,2,1,5,6,4]
    k = 2
    ob = Solution()
    ans = ob.findKthLargest(nums, k)
    print(ans)