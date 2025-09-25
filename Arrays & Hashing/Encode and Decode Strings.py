class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded = encoded + str(len(i)) + "#" + i
        return encoded

    def decode(self, s: str) -> List[str]:
        output = []
        start = 0
        while start < len(s):
            length = ""
            while s[start] != "#":
                length += s[start]
                start += 1
            length = int(length)
            output.append(s[start + 1:start + length + 1])
            start = start + length + 1
        return output

