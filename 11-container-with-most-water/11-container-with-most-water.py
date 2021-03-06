class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maximum = 0
        while left <= right:
            water = min(height[left],height[right]) * (right-left)
            maximum = max(maximum, water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return maximum