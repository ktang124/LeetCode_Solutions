class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        bCounter = [0] * 26
        for word in words2:
            cCounter = [0] * 26
            for c in word:
                aVal = ord(c) - ord('a')
                cCounter[aVal] += 1
                
            for i in range(26):
                bCounter[i] = max(bCounter[i],cCounter[i])
                
        res = []
        for word in words1:
            aCounter = [0] * 26
            for c in word:
                aVal = ord(c) - ord('a')
                aCounter[aVal] += 1
                
            shouldAdd = True
            for i, val in enumerate(bCounter):
                if val > aCounter[i]:
                    shouldAdd = False
                    
            if shouldAdd:
                res.append(word)
                
        return res
                
        