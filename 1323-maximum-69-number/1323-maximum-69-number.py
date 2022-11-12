class Solution:
    def maximum69Number (self, num: int) -> int:
        strNum = str(num)
        resList = []
        #change the first six into a nine
        changed = False
        for c in strNum:
            if c == '6' and not changed:
                resList.append('9')
                changed = True
            else:
                resList.append(c)
        return int(''.join(resList))
                