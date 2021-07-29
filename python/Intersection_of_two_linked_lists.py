# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        stack_a = []
        stack_b = []

        temp = headA
        while temp:
            stack_a.append(temp)
            temp = temp.next

        temp = headB
        while temp:
            stack_b.append(temp)
            temp = temp.next

        if len(stack_a) == 0 or len(stack_b) == 0 or stack_a[-1] != stack_b[-1]:
            return None

        prev = stack_a[-1]
        while len(stack_a) > 0 and len(stack_b) > 0 and stack_a[-1] == stack_b[-1]:
            prev = stack_a[-1]
            stack_a.pop()
            stack_b.pop()

        return prev


head1 = ListNode(4)
s = Solution()
s.getIntersectionNode()