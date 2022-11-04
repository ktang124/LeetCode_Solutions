class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        v = []
        for c in s:
            if c in vowels:
                v.append(c)
        nStr = []
        point = len(v)-1
        for c in s:
            if c in vowels:
                nStr.append(v[point])
                point -= 1
            else:
                nStr.append(c)
        return ''.join(nStr)