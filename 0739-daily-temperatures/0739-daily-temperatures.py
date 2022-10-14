class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * (len(temperatures))
        stack = deque()
        for i, temp in enumerate(temperatures):
            #if stack isn't empty and current temp is higher than top temp
            while stack and temp > temperatures[stack[-1]]:
                index = stack.pop()
                res[index] = i-index
                #this implies that top temp is greater than current temp
            stack.append(i)
                
        return res