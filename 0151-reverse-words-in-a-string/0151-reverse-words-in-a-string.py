class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        wordList = s.split()
        print(wordList)
        return ' '.join(wordList[::-1])