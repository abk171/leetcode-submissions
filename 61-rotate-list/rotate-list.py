# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        head_copy = head
        l = 0
        while head_copy:
            l += 1
            head_copy = head_copy.next
        
        k = k % l
        if k == 0:
            return head

        start_index = l - k - 1
        start_node = None

        head_copy = head

        while head_copy and start_index > 0:
            head_copy = head_copy.next
            start_index -= 1
        
        start_node = head_copy.next
        head_copy.next = None

        head_copy = start_node

        while start_node.next:
            start_node = start_node.next
        
        start_node.next = head
        head = head_copy

        return head