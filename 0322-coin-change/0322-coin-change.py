class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minCoins = [float('inf')] * (amount + 1)
        minCoins[0] = 0
        for i in range(1,amount+1):
            minCoins[i] = min((1+minCoins[i-coin] if i-coin>=0 else float('inf')) for coin in coins)
        return minCoins[amount] if minCoins[amount] != float('inf') else -1