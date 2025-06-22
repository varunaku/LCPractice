# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        stack = [(root,1)]

        while stack:
            node, depth = stack.pop()

            if node:
                max_depth = max(depth, max_depth)
                depth += 1
                stack.append((node.left, depth))
                stack.append((node.right, depth))

        return max_depth