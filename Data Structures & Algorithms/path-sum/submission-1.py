# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # currnt is the current sum of the leafs
        def dfs(node, current):
            if not node:
                return False
            #subtract from the current value
            current -= node.val

            #leaf check for if sum has hit zero(finding a path)
            if not node.left and not node.right:
                return current == 0

            #Not 0 and there are still nodes
            return dfs(node.left, current) or dfs(node.right, current)

        return dfs(root, targetSum) 


        