class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_valid(self, left_root, right_root):
        if left_root is None and right_root is None:
            return True
        if left_root is None or right_root is None:
            return False
        if left_root.val != right_root.val:
            return False

        if self.is_valid(left_root.right, right_root.left) is False:
            return False

        return self.is_valid(left_root.left, right_root.right)

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.is_valid(root.left, root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

s = Solution()
print(s.isSymmetric(root))