class Solution:
    # solution with O(nlogn) time complexity (depending on sorting algorithm) 
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
    
    # solution with O(n) time complexity. Identifying the starting of a sequence
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        seqList = []
        maxi = 0
        for i in store:
            seq = []
            if i-1 not in store:
                seq.append(i)
                while i+1 in store:
                    seq.append(i+1)
                    i = i+1
                seqList.append(seq)
        for i in range(len(seqList)):
            if len(seqList[i])>maxi:
                maxi = len(seqList[i])
        return maxi
