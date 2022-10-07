class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sCount = [0] * 26
        tCount = [0] * 26
        for i in range(len(s)):
            sCount[ord(s[i])- ord('a')] += 1
            tCount[ord(t[i]) - ord('a')] += 1
            
        diff = 0
        for i in range(26):
            diff += abs(sCount[i] - tCount[i])
            
        return diff//2