from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.inorder = None
        self.postorder = None

    def preorder(self, head):
        if head is None:
            print("null")
            return
        print(head.val)
        self.preorder(head.left)
        self.preorder(head.right)

    def build(self, inorder_left, inorder_right, postorder_left, postorder_right):
        if inorder_right - inorder_left < 0 or postorder_right - postorder_left < 0:
            return
        if inorder_right - inorder_left == 0:
            return TreeNode(self.postorder[postorder_right])

        head_index = inorder_left
        while head_index <= inorder_right and self.postorder[postorder_right] != self.inorder[head_index]:
            head_index += 1

        head = TreeNode(self.postorder[postorder_right])
        left_length = head_index - inorder_left

        head.left = self.build(inorder_left, inorder_left + left_length - 1, postorder_left, postorder_left + left_length - 1)
        head.right = self.build(head_index + 1, inorder_right, postorder_left + left_length, postorder_right - 1)

        return head

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.inorder = inorder
        self.postorder = postorder
        return self.build(0, len(inorder) - 1, 0, len(postorder) - 1)



s = Solution()
print(s.preorder(s.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])))
print(s.preorder(s.buildTree([2, 1], [2, 1])))
print(s.preorder(s.buildTree([1, 2], [2, 1])))
print(s.preorder(s.buildTree([2, 3, 1], [3, 2, 1])))
print(s.preorder(s.buildTree([1, 2, 3, 4], [4, 3, 2, 1])))
print(s.preorder(s.buildTree([1, 2, 3, 4], [1, 4, 3, 2])))
print(s.preorder(s.buildTree([1, 2, 3, 4, 5], [1, 4, 5, 3, 2])))