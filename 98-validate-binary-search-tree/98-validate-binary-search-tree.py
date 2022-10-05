# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lst):
            if root == None:
                return 
            dfs(root.left, lst)
            lst.append(root.val)
            dfs(root.right,lst)
            
        lst = []
        dfs(root, lst)
        for i in range(1, len(lst)):
            if lst[i] <= lst[i-1]:
                return False
            
        return True
            
        