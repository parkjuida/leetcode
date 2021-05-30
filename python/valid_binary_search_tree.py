class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    MIN = -2 ** 31 - 1
    MAX = 2 ** 31

    def is_valid(self, root, left_limit, right_limit):
        if root is None:
            return True

        if not right_limit > root.val > left_limit:
            return False

        if self.is_valid(root.left, left_limit, root.val) is False:
            return False
        if self.is_valid(root.right, root.val, right_limit) is False:
            return False

        return True

    def isValidBST(self, root: TreeNode) -> bool:
        return self.is_valid(root, self.MIN, self.MAX)


s = Solution()
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(s.isValidBST(root))
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(6)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
print(s.isValidBST(root))

root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(2)
print(s.isValidBST(root))

root = TreeNode(2**31 - 1)
print(s.isValidBST(root))