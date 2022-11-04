class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(s, i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i-=1
                j+=1
            return (i+1,j-1)
            #inclusive indices
        fTuple = (0,0)
        for i in range(len(s)):
            first, last = expand(s,i,i)
            diff = (fTuple[1]-fTuple[0])+1
            if (last-first)+1 > diff:
                fTuple = (first,last)
            first, last = expand(s,i,i+1)
            diff = (fTuple[1]-fTuple[0])+1
            if (last-first)+1 > diff:
                fTuple = (first,last)
        return s[fTuple[0]:fTuple[1]+1]
                
                