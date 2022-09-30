class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [(s[0],1)]
        for i in range(1, len(s)):
            if len(stack) > 0:
                prevC, count = stack[-1]
                if s[i] == prevC:
                    if count == k-1:
                        stack = stack[0:(len(stack)-(k-1))]
                    else:
                        stack.append((s[i],count+1))
                else:
                    
                    stack.append((s[i], 1))
            else:
                stack.append((s[i],1)) 
                    
        res = [a[0] for a in stack]
        resStr = "".join(res)
        return resStr