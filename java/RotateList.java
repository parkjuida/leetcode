public class RotateList {
    public ListNode rotateRight(ListNode head, int k) {
        if(head == null) return null;
        int listLength = 1;

        ListNode lastNode = head;

        while(lastNode != null && lastNode.next != null) {
            lastNode = lastNode.next;
            listLength++;
        }
        k = k % listLength;

        ListNode temp = head;

        for(int i = 0; i < listLength - k - 1; i++) {
            temp = temp.next;
        }
        lastNode.next = head;
        head = temp.next;
        temp.next = null;

        return head;
    }

    public void print(ListNode root) {
        while(root != null) {
            System.out.println(root.val);
            root = root.next;
        }
    }

    public static void main(String[] args) {
        RotateList rl = new RotateList();
        ListNode root = new ListNode(1);
        root.next = new ListNode(2);
        root.next.next = new ListNode(3);
        root.next.next.next = new ListNode(4);
        root.next.next.next.next = new ListNode(5);

        root = rl.rotateRight(root, 2);
        rl.print(root);

        root = new ListNode(0);
        root.next = new ListNode(1);
//        root.next.next = new ListNode(2);
        root = null;
        root = rl.rotateRight(root, 1);
        rl.print(root);
    }
}
