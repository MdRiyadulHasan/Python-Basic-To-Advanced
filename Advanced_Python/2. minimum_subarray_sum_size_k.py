def min_subarray_sum(arr, k):
    if k <= 0 or k > len(arr):
        return "Invalid input: k is out of range"

    windowSum = sum(arr[:k])
    maxSum = sum(arr[:k])
    for i in range(k, len(arr)):
        windowSum = windowSum + arr[i] - arr[i-k]
        maxSum = min(maxSum, windowSum)
    return maxSum
if __name__ == '__main__':
    arr = [-20, -61, 55, 41, 3, -29]
    k = 3
    result = min_subarray_sum(arr, k)
    print("Maximum subarray sum of size", k, "is:", result)