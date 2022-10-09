# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root == None:
            return False
        sortedList = []
        self.inOrder(root, sortedList)
        l = 0
        r = len(sortedList)-1
        while l < r:
            if sortedList[l] + sortedList[r] == k:
                return True
            elif sortedList[l] + sortedList[r] > k:
                #need to decrease
                r -= 1
            else:
                l += 1
                
        return False
    def inOrder(self, root, lst):
        if root == None:
            return
        self.inOrder(root.left, lst)
        lst.append(root.val)
        self.inOrder(root.right, lst)
        return