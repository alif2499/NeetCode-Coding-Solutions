class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            count[i] = 1 + count.get(i, 0)
        
        for num, count in count.items():
            freq[count].append(num)

        result = []
        for i in range(len(freq) -1, 0, -1):
            for j in freq[i]:
                result.append(j)
                if len(result) == k:
                    return result
                    