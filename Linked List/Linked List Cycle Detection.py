# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time complexity O(n) || Space complexity O(n)
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         visited = []
#         while head:
#             if head not in visited:
#                 visited.append(head)
#                 head = head.next
#             else:
#                 return True
#         return False

# Time complexity O(n) || Space complexity O(1)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False