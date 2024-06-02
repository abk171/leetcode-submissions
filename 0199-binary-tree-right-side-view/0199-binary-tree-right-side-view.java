/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        
        List<Integer> result = new ArrayList();
        if (root == null) {
            return result;
        }
        List<TreeNode> row = new ArrayList();
        List<TreeNode> temp = new ArrayList();
        

        row.add(root);
        
        while(row.size() > 0) {
            result.add(row.get(row.size() - 1).val);
            for (TreeNode node: row) {
                if (node.left != null) {
                    temp.add(node.left);
                }
                if (node.right != null) {
                    temp.add(node.right);
                }
                
            }
            // row = temp;
            
            row.clear();
            for (TreeNode node: temp) {
                row.add(node);
            }
            temp.clear();
        }
        
        
        return result;
    }
}