class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        temp = head
        length = 0
        stack = []

        while temp:
            temp = temp.next
            length += 1

        pre_length = 0
        temp = head
        while pre_length < (length - 1) // 2:
            stack.append(temp.val)
            pre_length += 1
            temp = temp.next

        stack.append(temp.val)
        if length % 2 == 0:
            temp = temp.next
        while temp:
            if temp.val != stack.pop():

                return False
            temp = temp.next

        return True


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(2)

s = Solution()
print(s.isPalindrome(head))