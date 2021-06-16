# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def build_root(self, preorder_left, preorder_right, inorder_left, inorder_right, preorder, inorder):
        if preorder_left > preorder_right or inorder_left > inorder_right:
            return None
        if preorder_left == preorder_right and inorder_left == inorder_right:
            return TreeNode(preorder[preorder_left])

        root_value = preorder[preorder_left]
        inorder_root_index = inorder_left

        while inorder_root_index < len(inorder) and inorder[inorder_root_index] != root_value:
            inorder_root_index += 1

        root = TreeNode(root_value)
        if inorder_root_index == inorder_left:
            root.right = self.build_root(preorder_left + 1, preorder_right, inorder_root_index + 1, inorder_right, preorder, inorder)
        elif inorder_root_index == inorder_right:
            root.left = self.build_root(preorder_left + 1, preorder_right, inorder_left, inorder_root_index - 1, preorder, inorder)
        else:
            root.left = self.build_root(
                preorder_left + 1, preorder_left + inorder_root_index - inorder_left, inorder_left, inorder_root_index - 1, preorder, inorder)
            root.right = self.build_root(
                preorder_left + inorder_root_index - inorder_left + 1, preorder_right, inorder_root_index + 1, inorder_right, preorder, inorder)

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.build_root(0, len(preorder) - 1, 0, len(inorder) - 1, preorder, inorder)



s = Solution()
s.buildTree([1], [1])
a = s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
a = s.buildTree([1, 2], [1, 2])
a = s.buildTree([1, 2, 3], [2, 3, 1])
a = s.buildTree([3, 2, 1, 4], [1, 2, 3, 4])
a