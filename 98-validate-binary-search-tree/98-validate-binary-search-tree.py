# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def _init_(self):
        self.last = float(-inf)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self._init_()
        def inorder(root):
            if root == None:
                return True
            left = inorder(root.left)
            cur = root.val > self.last
            self.last = root.val
            right = inorder(root.right)
        
            return (left and cur and right)
        return inorder(root)
    
                    
        