# solution with O(n) time and O(1) space, where n is the size of the input array.

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_capacity = 0
        left = 0
        right = len(heights)-1
        while left < right:
            if heights[left] <= heights[right]:
                capacity = heights[left] * (right - left)
                left += 1
            else:
                capacity = heights[right] * (right - left)
                right -= 1
            max_capacity = max(max_capacity, capacity)
        return max_capacity
