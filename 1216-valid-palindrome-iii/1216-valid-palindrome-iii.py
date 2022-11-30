class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        #recurrence relationship
        memo = [[float(inf)] * len(s) for _ in range(len(s))]
        def dfs(i, j):
            #print(s, k)
            if memo[i][j] != float('inf'):
                return memo[i][j]
            if i == j:
                return 0
            if i == j-1:
                return 0 if s[i] == s[j] else 1
            #case 1, l and r are the same
            if s[i] == s[j]:
                ans = dfs(i+1,j-1)
                memo[i][j] = ans
                return ans
            else:
                #either remove s[0] or remove s[-1]
                ans = 1+min(dfs(i+1,j),dfs(i,j-1))
                memo[i][j] = ans
                return ans
        return dfs(0,len(s)-1) <= k