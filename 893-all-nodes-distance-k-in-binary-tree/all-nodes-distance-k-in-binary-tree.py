# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        mat = {} # val -> []
        root_copy = root
        def dfs(n, p=None):
            if not n:
                return
            if p:
                mat[n.val] = [p.val]
            else:
                mat[n.val] = []
            if n.left:
                mat[n.val].append(n.left.val)
                dfs(n.left, n)
            if n.right:
                mat[n.val].append(n.right.val)
                dfs(n.right, n)
        
        dfs(root)

        bfs = [(k, target.val)]
        result = []
        
        while bfs:
            dist, n = bfs.pop(0)
            if dist == 0:
                result.append(n)
            for j in mat[n]:
                if j in mat:
                    bfs.append((dist - 1, j))
            del mat[n]

        return result