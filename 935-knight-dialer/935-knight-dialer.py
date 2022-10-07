class Solution:
    def knightDialer(self, n: int) -> int:
        moves = {1:[6,8], 2:[7,9],3:[4,8],4:[3,9,0],5:[],6:[7,1,0],7:[2,6],8:[1,3],9:[4,2],0:[4,6]}
        mod = 10 **9 +7
        total = 0
        #how many valid paths can we draw?
        counter = [1] * 10
        for i in range(1,n):
            nCounter = [0] * 10
            for num, count in enumerate(counter):
                 for index in moves[num]:
                    nCounter[index] += count
                    
                    
            counter = nCounter
        return (sum(counter) % mod)
                
            