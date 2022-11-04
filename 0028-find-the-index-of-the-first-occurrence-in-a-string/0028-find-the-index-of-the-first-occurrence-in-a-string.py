class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        end = (len(haystack) - len(needle))+1
        for i in range(end):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
            