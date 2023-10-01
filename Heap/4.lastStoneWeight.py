import heapq

class Solution:
    def lastStoneWeight(self, stones):
        # Convert stones to a max heap by negating the values
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            # Extract the two heaviest stones (negate them back)
            stone1 = -heapq.heappop(max_heap)
            stone2 = -heapq.heappop(max_heap)
            
            # Calculate the difference and add it back to the heap (negate it)
            diff = stone1 - stone2
            if diff != 0:
                heapq.heappush(max_heap, -diff)
        
        # If there's a stone left, return it (negate it back); otherwise, return 0
        return -max_heap[0] if max_heap else 0

# Example usage:
stones = [2, 7, 4, 1, 8, 1]
solution = Solution()
result = solution.lastStoneWeight(stones)
print("Last Stone Weight:", result)  # Output should be 1
