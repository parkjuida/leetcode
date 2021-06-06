# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_depth(self, root, height):
        if root is None:
            return 0
        return 1 + max(self.get_depth(root.left, height), self.get_depth(root.right, height))

    def maxDepth(self, root: TreeNode) -> int:
        return self.get_depth(root, 0)


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
s = Solution()
print(s.maxDepth(root))
root = TreeNode(1)
root.right = TreeNode(2)
print(s.maxDepth(root))
print(s.maxDepth(None))
root = TreeNode(0)
print(s.maxDepth(root))