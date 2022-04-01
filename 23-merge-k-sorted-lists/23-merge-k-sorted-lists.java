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
    public ListNode mergeKLists(ListNode[] lists) {
        
        if(lists.length == 0) return null;
        if(lists.length == 1) return lists[0];
        
        ListNode result = lists[0];
        for(int i = 1; i < lists.length; i++) {
            result = merge2Lists(result, lists[i]);
        }
        return result;
        
    }
    
    public ListNode merge2Lists(ListNode a, ListNode b) {
        ListNode result = new ListNode();
        ListNode ptr = result;
        int small;
        
        while(a != null || b!=null) {
            if(a == null) {
                ptr.next = b;
                return result.next;
            }
            else if(b == null) {
                ptr.next = a;
                return result.next;
            }
            
            else {
                if(a.val < b.val) {
                    small = a.val;
                    a = a.next;
                }
                else {
                    small = b.val;
                    b = b.next;
                }
                ptr.next = new ListNode(small);
                ptr = ptr.next;
            }
            
        }
        return result.next;
    }
}