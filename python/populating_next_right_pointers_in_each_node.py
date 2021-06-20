# Definition for a Node.
from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root

        depth = 1
        index = 0

        queue = deque()
        queue.append(root)

        prev_node = None

        while len(queue) > 0:
            node = queue.popleft()
            index += 1

            if depth == index:
                node.next = None
                if prev_node is not None:
                    prev_node.next = node
                prev_node = None
                depth = (depth + 1) * 2 - 1
            else:
                if prev_node is None:
                    prev_node = node
                else:
                    prev_node.next = node
                    prev_node = node

            if node.left is not None:
                queue.append(node.left)
                queue.append(node.right)

        return root


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
s = Solution()
s.connect(None)
s.connect(root)
