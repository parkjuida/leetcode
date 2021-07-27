# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        temp = head
        index = 0

        while temp and index < 10 ** 4 + 1:
            temp = temp.next

        if not temp:
            return False
        return True


s = Solution()
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
s.hasCycle(head)