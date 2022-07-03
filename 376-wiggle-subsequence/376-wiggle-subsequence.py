class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        dp = [0] * (len(nums))
        #build the diff array
        diffs = []
        for i in range(len(nums)-1):
            diffs.append(nums[i+1]-nums[i])
            
        prevPositive = False
        total = 1
        for i in range(len(diffs)):
            if prevPositive and diffs[i] < 0:
                total+= 1
                prevPositive = False
            elif not prevPositive and diffs[i] > 0:
                total += 1
                prevPositive = True
                
        prevPositive = True
        otherTotal = 1
        for i in range(len(diffs)):
            if prevPositive and diffs[i] < 0:
                otherTotal+= 1
                prevPositive = False
            elif not prevPositive and diffs[i] > 0:
                otherTotal += 1
                prevPositive = True
                
        return max(total,otherTotal)
            
                    