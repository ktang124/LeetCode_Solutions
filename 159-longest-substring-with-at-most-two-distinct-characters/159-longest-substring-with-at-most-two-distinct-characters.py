class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        charWindow = defaultdict(int)
        start = 0
        maximum = 0
        def verify(charWindow):
            count = 0
            for a in charWindow:
                if a > 0:
                    count += 1
            return count <= 2
        for end in range(len(s)):
            charWindow[s[end]] += 1
            while  not verify(charWindow.values()):
                charWindow[s[start]] -= 1
                start += 1
            maximum = max(maximum, end-start + 1)
            
        return maximum
            
                