# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if self.containsOne(root):
            root.left = self.pruneTree(root.left)
            root.right = self.pruneTree(root.right)
        else:
            return None
        
        return root
    
    def containsOne(self, root):
        if root == None:
            return False
        if root.val == 1:
            return True
        return self.containsOne(root.left) or self.containsOne(root.right)