class Solution:
    def countVowelPermutation(self, n: int) -> int:
        follows = {'a': 'e',
                   'e': 'ai',
                   'i': 'aeou',
                  'o': 'iu',
                  'u': 'a'}
        #character to set of characters
        states = defaultdict(int)
        #how many of these states are there?
        mod = 10 ** 9 + 7
        #base case
        for c in 'aeiou':
            states[c] += 1
        
        for i in range(n-1):
            newStates = defaultdict(int)
            for c in 'aeiou':
                numTransitions = 0
                for nextLetter in follows[c]:
                    newStates[nextLetter] += (states[c])
                    
            states = newStates
            
        total = sum(states.values())
        return (total % mod)
            
        