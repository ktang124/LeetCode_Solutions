# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        return self.helper(root)
    
    def helper(self, node):
        if not node:
            return None
        print(node.val)
        curr = self.helper(node.left)
        
        rt = self.helper(node.right)    
        node.right = curr
        if curr:
            while curr.right:
                curr = curr.right
                
        if curr:
            curr.right = rt
        else:
            node.right = rt
        node.left = None
        return node