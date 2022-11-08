class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        lowers = 'abcdefghijklmnopqrstuvwxyz'
        uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        for c in s:
            if not stack:
                stack.append(c)
            else:
                peek = stack[-1]
                if (c.isupper()):
                    if not (peek.islower() and peek.upper() == c):
                        stack.append(c)
                    else:
                        stack.pop()
                else:
                    if not (peek.isupper() and peek.lower() == c):
                        stack.append(c)
                    else:
                        stack.pop()
        return ''.join(stack)
                
                        
                    