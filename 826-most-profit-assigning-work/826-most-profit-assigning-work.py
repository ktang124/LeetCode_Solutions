class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        total = 0
        difficultyToProfit = defaultdict(lambda: 0)
        
        for idx, num in enumerate(difficulty):
            difficultyToProfit[num] = max(difficultyToProfit[num], profit[idx])
            
        difficulty.sort()
        newArr = [difficulty[0]]
        #only add the value in the newArr if an increase in difficulty results in increase in profit
        for i in range(1, len(difficulty)):
            if difficultyToProfit[difficulty[i]] > difficultyToProfit[newArr[-1]]:
                newArr.append(difficulty[i])
                
        worker.sort()
        i = 0
        best = 0
        for work in worker:
            while i < len(newArr) and work >= newArr[i]:
                best = max(best, difficultyToProfit[newArr[i]])
                i += 1
            total += best
       
            
        return total
            