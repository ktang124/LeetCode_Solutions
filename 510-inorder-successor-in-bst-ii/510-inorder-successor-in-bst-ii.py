"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
       
        if node == None:
            return None
        #case 1, the inorder successor is the minimum of the right node
        #case 2 the inorder successor is the parent because there is a leaf but the curNode must be on the left
        #case 3, the inorder successor is a parent but curnode is on the right
     
        if node.right != None:
            minimum = self.minimum(node.right)
            if minimum.val < node.val:
                return None
            else:
                return minimum
            
        else: 
            parent = node.parent
            if parent != None and node == parent.left:
                return parent
            else:
                return self.backtrack(node.parent, node.val)
        return None
        
    def minimum(self, node):
        if node == None:
            return None
        elif node.left == None:
            return node
        else:
            return self.minimum(node.left)
    def backtrack(self, node, val):
        if node == None:
            return None
        elif node.val > val:
            return node
        else:
            return self.backtrack(node.parent, val)
        