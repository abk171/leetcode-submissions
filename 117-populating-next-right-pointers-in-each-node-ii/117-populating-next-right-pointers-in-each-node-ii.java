/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
      if(root == null) return root;
      Node currNode = root;
      while(currNode != null) {
        Node dummyNode = new Node(0);
        Node prevNode = dummyNode;
        while(currNode != null) {
          if(currNode.left != null) {
            prevNode.next = currNode.left;
            prevNode = currNode.left;
          }
          if(currNode.right != null) {
            prevNode.next = currNode.right;
            prevNode = currNode.right;
          }
          currNode = currNode.next;
        }
        currNode = dummyNode.next;
      }
      return root;
    }
}