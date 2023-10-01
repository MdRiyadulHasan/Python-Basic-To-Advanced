import heapq

def find_k_smallest_elements(arr, k):
    # Create a min heap and initialize it with the first k elements
    # min_heap = arr[:k]
    # heapq.heapify(min_heap)
    
    # # Iterate through the remaining elements
    # for element in arr[k:]:
    #     # If the current element is smaller than the largest element in the heap,
    #     # replace the largest element with the current element
    #     if element < min_heap[0]:
    #         heapq.heappop(min_heap)
    #         heapq.heappush(min_heap, element)
    
    # return min_heap
    heapq.heapify(arr)
    k_smallest = heapq.nsmallest(k, arr)
    return k_smallest

# Sample dataset
data = [12, 6, 2, 8, 23, 4, 7, 3, 10, 1, 19]

# Find the 3 smallest elements
k = 3
result = find_k_smallest_elements(data, k)

print(f"The {k} smallest elements are:", result)
