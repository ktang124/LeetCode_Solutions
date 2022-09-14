# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        counter = [0] * 10
        if root == None:
            return 0
        def dfs(root, counter):
            if root.left == None and root.right == None:
                #count number of odds and evens
                counter[root.val] += 1
                countOdd = 0
                for i in range(1,10):
                    if counter[i] % 2 != 0:
                        countOdd += 1
                        
                counter[root.val] -= 1
                if countOdd <= 1:
                    return 1
                else:
                    return 0
            else:
                total = 0
                counter[root.val] += 1
                if root.left != None:  
                    total += dfs(root.left, counter)
                if root.right != None:
                    total += dfs(root.right, counter)
                counter[root.val] -= 1
                return total
           
        return dfs(root, counter)
                        
            