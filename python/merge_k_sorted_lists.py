from queue import PriorityQueue


# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.head = None
        self.tail = None
        self.pq = PriorityQueue()

    def create_answer_node(self, value):
        temp = ListNode(value)

        if self.head is None:
            self.head = temp
            self.tail = self.head
        else:
            self.tail.next = temp
            self.tail = self.tail.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        for index, _list in enumerate(lists):
            if _list is not None:
                self.pq.put((_list.val, index))
                lists[index] = lists[index].next

        while not self.pq.empty():
            value, index = self.pq.get()
            self.create_answer_node(value)
            if lists[index] is not None:
                self.pq.put((lists[index].val, index))
                lists[index] = lists[index].next

        return self.head


s = Solution()
a = ListNode(1)
a.next = ListNode(4)
a.next.next = ListNode(5)
b = ListNode(1)
b.next = ListNode(3)
b.next.next = ListNode(4)
c = ListNode(2)
c.next = ListNode(6)

answer = s.mergeKLists([a, b, c])
while answer is not None:
    print(answer.val)
    answer = answer.next

s = Solution()
answer = s.mergeKLists([])

while answer is not None:
    print(answer.val)
    answer = answer.next

s = Solution()
answer = s.mergeKLists([ListNode()])

while answer is not None:
    print(answer.val)
    answer = answer.next