import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        head = ListNode(None)
        curr = head
        h = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))  # Push (val, index) tuple
                lists[i] = lists[i].next
        
        while h:
            val, i = heapq.heappop(h)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))  # Push (val, index) tuple
                lists[i] = lists[i].next
        
        return head.next  # Return the merged linked list

if __name__ == "__main__":
    # Create linked lists
    list1 = ListNode(1, ListNode(4, ListNode(5)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    list3 = ListNode(2, ListNode(6))
    
    lists = [list1, list2, list3]
    
    ob = Solution()
    ans = ob.mergeKLists(lists)
    
    # Print the merged linked list
    while ans:
        print(ans.val, end=" -> ")
        ans = ans.next
