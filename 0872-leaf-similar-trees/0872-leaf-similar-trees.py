# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getLeaves(self, root, leaves):
        if not root:
            return
        if not root.left and not root.right:
            leaves.append(root.val)
        self.getLeaves(root.left, leaves)
        self.getLeaves(root.right, leaves)
        
        
    
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaf1 = []
        leaf2 = []
        
        self.getLeaves(root1, leaf1)
        self.getLeaves(root2, leaf2)
        
        if len(leaf1) != len(leaf2):
            return False
        
        for i in range(len(leaf1)):
            if leaf1[i] != leaf2[i]:
                return False
        return True