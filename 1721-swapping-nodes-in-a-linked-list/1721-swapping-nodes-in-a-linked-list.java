/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapNodes(ListNode head, int k) {
        ListNode leftPtr = head;
        ListNode rightPtr = head;
        ListNode left = head;
        
        for(int i = 0; i < k - 1; i++) {
            leftPtr = leftPtr.next;            
        }
        left = leftPtr;
        
        while(leftPtr.next != null) {
            leftPtr = leftPtr.next;
            rightPtr = rightPtr.next;
        }
        
        int temp = left.val;
        left.val = rightPtr.val;
        rightPtr.val = temp;
        
        return head;
        
    }
}