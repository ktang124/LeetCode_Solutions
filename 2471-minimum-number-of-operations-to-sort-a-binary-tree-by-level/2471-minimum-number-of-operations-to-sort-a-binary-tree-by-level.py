# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def minSwap(arr, n):
     
            ans = 0
            temp = arr.copy()

            # Dictionary which stores the
              # indexes of the input array
            h = {}

            temp.sort()

            for i in range(n):

                #h.[arr[i]
                h[arr[i]] = i

            init = 0

            for i in range(n):

                # This is checking whether
                # the current element is
                # at the right place or not
                if (arr[i] != temp[i]):
                    ans += 1
                    init = arr[i]

                    # If not, swap this element
                      # with the index of the
                      # element which should come here
                    arr[i], arr[h[temp[i]]] = arr[h[temp[i]]], arr[i]

                    # Update the indexes in
                      # the hashmap accordingly
                    h[init] = h[temp[i]]
                    h[temp[i]] = i

            return ans
        minOps = 0
        queue = [root]
        while queue:
            size = len(queue)
            curLevel = []
            while size:
                size -= 1
                poll = queue.pop(0)
                if poll.left:
                    queue.append(poll.left)
                if poll.right:
                    queue.append(poll.right)
                curLevel.append(poll.val)
            minOps += minSwap(curLevel, len(curLevel))
                
        return minOps
        
        