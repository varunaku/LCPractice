# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if not root:
        #     # do nothing
        #     return root
        # else:
        #     root.left, root.right = root.right, root.left
        #     self.invertTree(root.left)
        #     self.invertTree(root.right)
           
        #     return root

        def dfs(node):
            if not node: 
                return
            
            temp = node.left
            node.left = node.right
            node.right = temp

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        return root