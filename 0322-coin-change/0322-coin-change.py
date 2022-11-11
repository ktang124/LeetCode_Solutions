class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: #fired by twitter edition
        minCoins =  [0] + ([float('inf')] * (amount))
        for i in range(1,amount+1): minCoins[i] = 1+min((minCoins[i-coin] if i-coin>=0 else float('inf')) for coin in coins)
        return minCoins[amount] if minCoins[amount] != float('inf') else -1