class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        l,r = 0,0
        mostFreq = 0
        result = 0
        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r],0)
            while (r-l+1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l+=1
            result = max(result, r-l+1)
        return result

        