import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):
        
        taskCount = Counter(tasks)
        max_heap = [(-count, task) for task, count in taskCount.items()]
        heapq.heapify(max_heap)
        
        time = 0
        
        while max_heap:
            tmp = []
            
            for _ in range(n + 1):  # Process tasks for n+1 cycles.
                if max_heap:
                    count, task = heapq.heappop(max_heap)
                    count = count + 1
                    tmp.append((count, task))
                else:
                    break
                
            for count, task in tmp:
                if count + 1 < 0:
                    heapq.heappush(max_heap, (count + 1, task))  # Add remaining tasks back to the heap.
            
            # For every cycle, we add n+1 cycles to the total time.
            # However, if the heap is empty after processing, we add the length of tmp to the time.
            time += len(tmp) if not max_heap else n + 1
                
        return time
tasks = ["A","A","A","B"]
n = 2
solution = Solution()
result = solution.leastInterval(tasks, n)
print("Minimum Time Slots:", result)  # Output should be 8
