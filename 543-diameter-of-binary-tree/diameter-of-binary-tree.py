# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # whats the algo
        # 4 -> 0, 0
        # 5 -> 0, 0

        # 2 -> 1, 1
        # 3 -> 0 , 0

        # 1 -> max(left, right) + 1, 1
        # base case: return 0 if no kids
        # if kids, add 1
        # max(path_length, left+right) at each node, in case the lefts and rights combine into something crazy
        self.path_length_thru = 0
        def dfs(node):
            if node is None: 
                return 0
            
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            self.path_length_thru = max(left_depth + right_depth, self.path_length_thru)

            return max(left_depth, right_depth) +1

        dfs(root)
        return self.path_length_thru