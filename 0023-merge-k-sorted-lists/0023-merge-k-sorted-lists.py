# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwo(a, b):
            res = ListNode(0)
            rptr = res
            while a or b:
                
                if not a:
                    rptr.next = b
                    b = None
                    
                elif not b:
                    rptr.next = a
                    a = None
                
                else:
                    if a.val < b.val:
                        rptr.next = ListNode(a.val)
                        a = a.next
                    else:
                        rptr.next = ListNode(b.val)
                        b = b.next
                rptr = rptr.next
            return res.next
        
        def divide(ptrs):
            lp = len(ptrs)
            if lp == 2:
                return mergeTwo(ptrs[0], ptrs[1])
            elif lp == 1:
                return ptrs[0]
            elif lp == 0:
                return None
            
            left = ptrs[0 : lp // 2]
            right = ptrs[lp // 2 : ]
            
            return mergeTwo(divide(left), divide(right))

        return divide(lists)
        # return mergeTwo(lists[0], lists[1])

        # return ListNode(0)
            
                    
                    
            