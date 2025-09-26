class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start < end:
            if not s[start].isalnum():
                while not s[start].isalnum() and start<end:
                    start += 1
            if not s[end].isalnum():
                while not s[end].isalnum() and end>start:
                    end -= 1
            if s[start].isalnum() and s[end].isalnum():
                if s[start].lower() == s[end].lower():
                    start += 1
                    end -= 1
                else:
                    return False
        return True