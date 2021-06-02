from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        q = deque()

        current_level = 0
        q.append((root, current_level))
        answer = []
        current_answer = []

        while len(q) > 0:
            node, level = q.popleft()
            if level == current_level:
                current_answer.append(node.val)
            else:
                answer.append(current_answer)
                current_answer = [node.val]
                current_level += 1

            if node.left is not None:
                q.append((node.left, level + 1))
            if node.right is not None:
                q.append((node.right, level + 1))

        if len(current_answer) > 0:
            answer.append(current_answer)

        return answer


r = TreeNode(3)
r.left = TreeNode(9)
r.right = TreeNode(20)
r.right.left = TreeNode(15)
r.right.right = TreeNode(7)
s = Solution()
print(s.levelOrder(r))