# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_next(self, current_level, stack, queue):
        if current_level % 2 == 1:
            return stack.pop()
        else:
            return queue.pop()

    def append(self, current_level, stack, queue, node):
        if current_level % 2 == 0:
            stack.append(node.left)
            stack.append(node.right)
        else:
            queue.append(node.right)
            queue.append(node.left)

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        queue = deque()
        stack = deque()
        queue.append(root)
        total_answer = []
        level_answer = []
        current_level = 0

        while len(queue) > 0 or len(stack) > 0:
            if (len(queue) == 0 and current_level % 2 == 0) or (len(stack) == 0 and current_level % 2 == 1):
                total_answer.append(level_answer)
                level_answer = []
                current_level += 1
                continue
            node = self.get_next(current_level, stack, queue)
            if node is None:
                continue
            level_answer.append(node.val)
            self.append(current_level, stack, queue, node)

        if len(level_answer) > 0:
            total_answer.append(level_answer)

        return total_answer


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

s = Solution()
print(s.zigzagLevelOrder(root))

root = TreeNode()
print(s.zigzagLevelOrder(None))

root = TreeNode(1)
print(s.zigzagLevelOrder(root))
