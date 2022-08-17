class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alpha = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transforms = set()
        for word in words:
            morse = ""
            for c in word:
                index = ord(c) - ord('a')
                morse += alpha[index]
            transforms.add(morse)
            
        return len(transforms)