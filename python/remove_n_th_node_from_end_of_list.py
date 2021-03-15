# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l = head
        sequence = []
        while l is not None:
            sequence.append(l)
            l = l.next

        sequence_length = len(sequence)

        if sequence_length - n - 1 < 0:
            head = sequence[0].next
        elif sequence_length - n + 1 < sequence_length:
            sequence[sequence_length - n - 1].next = sequence[sequence_length - n + 1]
        else:
            sequence[sequence_length - n - 1].next = None
        return head


l5 = ListNode(5)
l4 = ListNode(4, l5)
l3 = ListNode(3, l4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)

s = Solution()
l = s.removeNthFromEnd(l1, 2)

while l is not None:
    print(l.val)
    l = l.next

s = Solution()
l1 = ListNode(1)
l = s.removeNthFromEnd(l1, 1)


while l is not None:
    print(l.val)
    l = l.next

s = Solution()
l2 = ListNode(2)
l1 = ListNode(1, l1)
l = s.removeNthFromEnd(l1, 1)


while l is not None:
    print(l.val)
    l = l.next
