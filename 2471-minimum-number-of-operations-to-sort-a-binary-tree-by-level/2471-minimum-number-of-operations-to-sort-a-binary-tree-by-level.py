# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def minSwaps(nums):
            Len = len(nums)
            map = {}
            for i in range(Len):
                map[nums[i]] = i

            nums = sorted(nums)

            # To keep track of visited elements. Initialize
            # all elements as not visited or false.
            visited = [False for col in range(Len)]

            # Initialize result
            ans = 0
            for i in range(Len):

                # already swapped and corrected or
                # already present at correct pos
                if (visited[i] or map[nums[i]] == i):
                    continue

                j,cycle_size = i, 0
                while (visited[j] == False):
                    visited[j] = True

                    # move to next node
                    j = map[nums[j]]
                    cycle_size += 1

                # Update answer by adding current cycle.
                if (cycle_size > 0):
                    ans += (cycle_size - 1)
 
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
            minOps += minSwaps(curLevel)
                
        return minOps
        
        