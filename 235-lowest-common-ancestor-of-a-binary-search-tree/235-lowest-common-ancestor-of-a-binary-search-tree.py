# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def traverse(root):
            if root == None:
                return False
            left = traverse(root.left)
            right = traverse(root.right)
            mid = root == p or root == q
            
            if mid + left + right >= 2:
                self.ans = root
            return mid or left or right
        traverse(root)
        return self.ans
        