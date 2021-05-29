from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        visited = set()
        if root is None:
            return []
        stack = [root]
        answer = []
        while len(stack) != 0:
            current_node = stack.pop()
            if current_node is None:
                continue

            if current_node.left is None or current_node.left in visited:
                answer.append(current_node.val)
                visited.add(current_node)
                if not (current_node.right is None or current_node.right in visited or current_node.right in stack):
                    stack.append(current_node.right)
            else:
                stack.append(current_node.right)
                stack.append(current_node)
                stack.append(current_node.left)

        return answer


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
s = Solution()
print(s.inorderTraversal(root))
root = None
print(s.inorderTraversal(root))
root = TreeNode(1)
print(s.inorderTraversal(root))
root = TreeNode(1)
root.left = TreeNode(2)
print(s.inorderTraversal(root))
root = TreeNode(1)
root.right = TreeNode(2)
print(s.inorderTraversal(root))
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
print(s.inorderTraversal(root))