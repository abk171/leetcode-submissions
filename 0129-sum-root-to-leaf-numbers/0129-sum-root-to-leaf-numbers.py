# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def accumulate(node, acc):
            if not node:
                return 0
            acc = acc * 10 + node.val
            if not node.right and not node.left:
                return acc
            return accumulate(node.left, acc) + accumulate(node.right, acc)
        
        return accumulate(root, 0)