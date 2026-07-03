"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        #stores values that we have visited after checking that they have no children
        result = []
        
        def helper(node):
            if not node:
                return
            for c in node.children:
                helper(c)
            result.append(node.val)
        
        helper(root)
        return result
            
        