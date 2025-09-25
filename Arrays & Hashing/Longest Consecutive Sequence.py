class Solution:
    # solution with nlogn time complexity (depending on sorting algorithm) 
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = 1
        longest = 0
        nums=sorted(set(nums))
        if len(nums)==1:
            return 1
        for i in range(len(nums)-1):
            if abs(nums[i+1] - nums[i]) == 1:
                seq +=1
                if longest < seq:
                    longest = seq
            else:
                if longest < seq:
                    longest = seq
                seq = 1
        return longest