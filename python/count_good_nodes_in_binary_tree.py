# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find(self, root, current_max):
        answer = 0
        if root.val >= current_max:
            current_max = root.val
            answer = 1
        answer += self.find(root.left, current_max) if root.left is not None else 0
        answer += self.find(root.right, current_max) if root.right is not None else 0

        return answer

    def goodNodes(self, root: TreeNode) -> int:
        return self.find(root, -10 ** 4)
