"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
    
        old_to_new = {}

        head_copy = head

        while head:
            old_to_new[head] = Node(head.val)
            head = head.next
        
        new_head = old_to_new[head_copy]

        while head_copy:
            new_node = old_to_new[head_copy]
            new_random = old_to_new[head_copy.random] if head_copy.random else None
            new_next = old_to_new[head_copy.next] if head_copy.next else None

            new_node.next = new_next
            new_node.random = new_random

            head_copy = head_copy.next
        
        return new_head