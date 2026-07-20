# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #recursive helper function
        def valid(node, left, right):
            if not node:
                return True
            if not(left < node.val < right):
                return False
            #recursive step
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        #compare with the min and max float value possible to start
        return valid(root, float("-inf"), float("inf"))
        