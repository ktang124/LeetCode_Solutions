class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        def match(word, pattern):
            mapping1 = {}
            used = set()
            for i, pat in enumerate(pattern):
                char = word[i]
                if pat not in mapping1:
                    if char in used:
                        return False
                    mapping1[pat] = char
                    used.add(char)
                else:
                    if char != mapping1[pat]:
                        return False

            return True
        for word in words:
            if match(word, pattern):
                res.append(word)
                
        return res