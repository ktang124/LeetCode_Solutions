class Solution:
    def romanToInt(self, s: str) -> int:
        translation = {'I': 1,
                      'V': 5,
                      'X': 10,
                      'L': 50,
                      'C': 100,
                      'D': 500,
                      'M': 1000,
                      'IV': 4,
                      'IX': 9,
                       'XL': 40,
                      'XC': 90,
                      'CD': 400,
                      'CM': 900}
        num = 0
        i = 0
        while i < len(s):
            char = s[i]
            chunk = s[i:i+2]
            if chunk in translation:
                num += translation[chunk]
                i += 2
            else:
                num += translation[char]
                i += 1
        return num