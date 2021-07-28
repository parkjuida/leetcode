# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_sort(self, head):
        head_length = 0
        temp = head

        while temp:
            head_length += 1
            temp = temp.next

        if head_length <= 1:
            return head

        left = head
        left_length = 0
        temp = head
        while left_length < (head_length // 2) - 1:
            left_length += 1
            temp = temp.next

        right = temp.next
        temp.next = None
        left = self.merge_sort(left)
        right = self.merge_sort(right)

        return self.quanquer(left, right)

    def quanquer(self, left, right):
        temp_left = left
        temp_right = right
        merged = None
        temp_merged = merged
        while temp_left and temp_right:
            if temp_left.val < temp_right.val:
                if merged:
                    temp_merged.next = temp_left
                    temp_merged = temp_merged.next
                else:
                    merged = temp_left
                    temp_merged = merged
                temp_left = temp_left.next
            else:
                if merged:
                    temp_merged.next = temp_right
                    temp_merged = temp_merged.next
                else:
                    merged = temp_right
                    temp_merged = merged
                temp_right = temp_right.next

        while temp_left:
            temp_merged.next = temp_left
            temp_left = temp_left.next
            temp_merged = temp_merged.next

        while temp_right:
            temp_merged.next = temp_right
            temp_right = temp_right.next
            temp_merged = temp_merged.next

        return merged

    def sortList(self, head: ListNode) -> ListNode:
        return self.merge_sort(head)


h = ListNode(-1)
h.next = ListNode(5)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)
h.next.next.next.next = ListNode(0)
s = Solution()
r = s.sortList(h)
while r:
    print(r.val)
    r = r.next
