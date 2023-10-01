import heapq
def maxSlidingWindow(nums, k):
    if k == 1:
        return nums  # If the window size is 1, the maximum value is the number itself
    
    rwindow = [(-val, i) for i, val in enumerate(nums[:k])]  # Create a max heap of the first window
    heapq.heapify(rwindow)  # Heapify the initial window

    res = [-rwindow[0][0]]  # Initialize the result list with the maximum value of the first window

    for i in range(k, len(nums)):
        while rwindow[0][1] <= i - k:
            heapq.heappop(rwindow)  # Remove elements that are out of the current window
        heapq.heappush(rwindow, (-nums[i], i))  # Push the current element and its index to the max heap
        res.append(-rwindow[0][0])  # Append the maximum element (negated) of the current window to the result list

    return res
k = 3
nums = [1,3,-1,-3,5,3,6,7]
ans = maxSlidingWindow(nums,k)
print(ans)
