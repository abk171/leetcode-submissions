# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        tree = []
        
        def inorder(node):
            if node:
                inorder(node.left)
                tree.append(node.val)
                inorder(node.right)
        
        
        inorder(root)
        diff = 10 ** 5 + 1
        for i in range(1, len(tree)):
            diff = min(diff, tree[i] - tree[i - 1])
        
        print(tree)
        return diff