class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s = 0
        #initial even sums
        for n in nums:
            if n % 2== 0:
                s += n
        res = []
        for val, index in queries:
            #need to check if num was even or odd before
            if nums[index] % 2 == 0:
                #we have already added the sum
                prev = nums[index]
                nums[index] += val
                if nums[index] % 2 == 0:
                    s += val
                else:
                    s -= prev
            else:
                #we have not added the sum
                nums[index] += val
                if nums[index] % 2 ==0:
                    s += nums[index]
                    
            res.append(s)
        return res
                    
            
                