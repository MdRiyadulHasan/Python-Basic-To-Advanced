import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, S: str) -> str:
        # Count the frequency of each character in the string
        char_count = Counter(S)
        
        # Create a max heap (priority queue) to store characters by their frequency
        max_heap = [(-freq, char) for char, freq in char_count.items()]
        heapq.heapify(max_heap)
        
        result = []
        
        while len(max_heap) >= 2:
            # Pop the two most frequent characters from the heap
            freq1, char1 = heapq.heappop(max_heap)
            freq2, char2 = heapq.heappop(max_heap)
            
            # Append the characters to the result while ensuring they are not adjacent
            result.extend([char1, char2])
            
            # Decrease the frequencies and re-insert the characters if they are not exhausted
            if freq1 < -1:
                heapq.heappush(max_heap, (freq1 + 1, char1))
            if freq2 < -1:
                heapq.heappush(max_heap, (freq2 + 1, char2))
        
        # If there is one character left with a frequency of -1, append it to the result
        if max_heap:
            freq, char = heapq.heappop(max_heap)
            if freq < -1:
                return ""
            result.append(char)
        
        return ''.join(result)

# Example usage:
s = "aabb"
solution = Solution()
result = solution.reorganizeString(s)
print("Reorganized String:", result)  # Output should be "aba"
