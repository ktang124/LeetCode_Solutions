class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sortStrings = sorted(strs)
        top = sortStrings[0]
        bot = sortStrings[len(strs)-1]
        n = min(len(top),len(bot))
        i = 0
        while i < n and top[i] == bot[i]:
            i += 1
            
        return top[:i]