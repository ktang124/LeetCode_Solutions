class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        #recurrence relationship
        dp = {}
        def dfs(s, k, dp):
            #print(s, k)
            if (s,k) in dp:
                return dp[(s,k)]
            if len(s) <= 1:
                return True
            #case 1, l and r are the same
            if s[0] == s[-1]:
                inbetween = s[1:len(s)-1]
                ans = dfs(inbetween, k,dp)
                dp[(s,k)] = ans
                return ans
            else:
                #either remove s[0] or remove s[-1]
                if k == 0:
                    return False
                remStart = s[1:]
                remLast = s[0:len(s)-1]
                ans = dfs(remStart, k-1,dp) or dfs(remLast,k-1,dp)
                dp[(s,k)] = ans
                return ans
        return dfs(s,k,dp)