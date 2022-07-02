class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = defaultdict(lambda: 0)
        for c in s:
            counts[c] += 1
        for c in t:
            counts[c] -= 1
            
        for n in counts:
            if counts[n] != 0:
                return False
        
        return True