class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = 'aeiouAEIOU'
        half = (len(s))//2
        a= s[0:half]
        b = s[half:]
        aCount = Counter(a)
        bCount = Counter(b)
        aVowels = 0
        bVowels = 0
        for v in vowels:
            aVowels += aCount[v]
            bVowels += bCount[v]
        return aVowels == bVowels
        