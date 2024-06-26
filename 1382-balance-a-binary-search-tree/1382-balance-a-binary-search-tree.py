# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        
        def inorder(node):
            if not node:
                return
            
            if node.left:
                inorder(node.left)
            
            arr.append(node.val)
            
            if node.right:
                inorder(node.right)
        
        inorder(root)
        
        def balance(arr, left, right):
            if left > right:
                return None
        
            mid = (left + right) // 2
            
            lt = balance(arr, left, mid - 1)
            rt = balance(arr, mid + 1, right)
            
            return TreeNode(arr[mid], lt, rt)
        
        return balance(arr, 0, len(arr) - 1)
            