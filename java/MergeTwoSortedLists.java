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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode res = null;
        ListNode tempLast = null;
        int thisVal = 0;

        while(l1 != null && l2 != null) {
            if(l1.val > l2.val) {
                if(res == null) {
                    res = l2;
                    tempLast = res;
                } else {
                    tempLast.next = l2;
                    tempLast = tempLast.next;
                }
                l2 = l2.next;
            } else {
                if(res == null) {
                    res = l1;
                    tempLast = res;
                } else {
                    tempLast.next = l1;
                    tempLast = tempLast.next;
                }
                l1 = l1.next;
            }
        }

        while(l1 != null) {
            if(res == null) {
                res = l1;
                tempLast = res;
            } else {
                tempLast.next = l1;
                tempLast = tempLast.next;
            }
            l1 = l1.next;
        }
        while(l2 != null) {
            if(res == null) {
                res = l2;
                tempLast = res;
            } else {
                tempLast.next = l2;
                tempLast = tempLast.next;
            }
            l2 = l2.next;
        }

        return res;
    }
}