"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None:
            return []
        res = []
        queue = [root]
        while queue:
            size = len(queue)
            levelLst = []
            while size:
                size -= 1
                poll = queue.pop(0)
                levelLst.append(poll.val)
                for c in poll.children:
                    queue.append(c)
            res.append(levelLst)
            
        return res
                