class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        temp = head
        l = []

        while temp:
            l.append(temp)
            temp = temp.next

        index_hash = dict([(instance, index) for index, instance in enumerate(l)])

        new_list = []
        temp = head
        prev = None
        while temp:
            new_node = Node(temp.val)
            new_list.append(new_node)
            if prev:
                prev.next = new_node
            prev = new_node
            temp = temp.next

        temp = head
        index = 0
        while temp:
            if temp.random:
                new_list[index].random = new_list[index_hash[temp.random]]
            index += 1
            temp = temp.next

        if len(new_list) == 0:
            return None
        return new_list[0]


s = Solution()
head = Node(7)
head.next = Node(13)
head.next.next = Node(11)
head.next.next.next = Node(10)
head.next.next.next.next = Node(1)
head.next.random = head
head.next.next.random = head.next.next.next.next
head.next.next.next.random = head.next.next
head.next.next.next.next.random = head
t = s.copyRandomList(head)

while t:
    if t.random is not None:
        print(t.val, t.random.val)
    else:
        print(t.val, None)
    t = t.next

t = s.copyRandomList(None)