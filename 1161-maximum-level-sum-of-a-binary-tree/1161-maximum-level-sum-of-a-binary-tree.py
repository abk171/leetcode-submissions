# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sums = []

        def traverse(node, i):
            if not node:
                return
            if len(sums) <= i:
                sums.append(node.val)
            else:
                sums[i] = sums[i] + node.val
            traverse(node.left, i + 1)
            traverse(node.right, i + 1)
        
        traverse(root, 0)

        index = 0
        msum = sums[0]
        for i, s in enumerate(sums):
            if msum < s:
                index = i
                msum = s
        
        return index + 1