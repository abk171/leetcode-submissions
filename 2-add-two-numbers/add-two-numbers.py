# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        result_ptr = result
        s = 0
        c = 0
        while l1 or l2:
            s = c
            c = 0
            if l1:
                s += l1.val
                l1 = l1.next
            
            if l2:
                s += l2.val
                l2 = l2.next
            
            c = s // 10
            s = s % 10
            result_ptr.next = ListNode(s)
            result_ptr = result_ptr.next

        if c == 1:
            result_ptr.next = ListNode(1)
        return result.next