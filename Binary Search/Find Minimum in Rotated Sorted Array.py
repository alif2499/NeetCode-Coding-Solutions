class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] > nums[0]:
            return nums[0]
        elif len(nums) == 1:
            return nums[0]
        else:
            right = len(nums) - 1
            left  = 0
            while nums[left] > nums[right]:
                mid = (left + right) // 2
                if nums[mid] > nums[right]:
                    left = mid
                else:
                    right = mid
            return nums[mid]