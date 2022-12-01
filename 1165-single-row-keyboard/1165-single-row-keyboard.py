class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        cToIndex = {}
        for i,c in enumerate(keyboard):
            cToIndex[c] = i
        curIndex = 0
        total = 0
        for c in word:
            move = abs(curIndex-cToIndex[c])
            total += move
            curIndex = cToIndex[c]
        return total