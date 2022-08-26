class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countRansom = [0] * 26
        countMag = [0] * 26
        for c in ransomNote:
            countRansom[ord(c)-ord('a')] += 1
        for c in magazine:
            countMag[ord(c)-ord('a')] += 1
            
        for i in range(26):
            if countRansom[i] > countMag[i]:
                return False
            
        return True