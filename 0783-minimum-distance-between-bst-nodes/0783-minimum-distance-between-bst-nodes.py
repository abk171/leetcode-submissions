import queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        arr = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        mindiff = arr[1] - arr[0]
        
        for i in range(1, len(arr)):
            mindiff = min(mindiff, arr[i] - arr[i - 1])
        
        return mindiff
            
            