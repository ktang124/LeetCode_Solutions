class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def dfs(s, i, ans, curArr):
            if i == len(s):
                if len(curArr) > 0:
                    ans.append(list(curArr))
                return
            for j in range(i, len(s)):
                curSlice = s[i:j+1]
                if curSlice[::-1] == curSlice:
                    curArr.append(curSlice)
                    dfs(s,j+1,ans,curArr)
                    curArr.pop()
        dfs(s, 0, ans, [])
        return ans