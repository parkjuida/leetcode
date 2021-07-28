# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        values = []

        temp = head
        while temp:
            values.append(temp.val)
            temp = temp.next

        temp = head
        values.sort()

        for value in values:
            temp.val = value
            temp = temp.next

        return head


h = ListNode(4)
h.next = ListNode(2)
h.next.next = ListNode(1)
h.next.next.next = ListNode(3)
s = Solution()
r = s.sortList(h)
while r:
    print(r.val)
    r = r.next
