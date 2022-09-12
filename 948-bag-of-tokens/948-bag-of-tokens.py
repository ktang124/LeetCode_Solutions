class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        sortedToks = sorted(tokens)
        left = 0
        right = len(sortedToks)-1
        p = power
        score = 0
        if len(tokens) == 1:
            return 1 if power > tokens[0] else 0 
        while left <= right:
            if power >= sortedToks[left]:
                score += 1
                power -= sortedToks[left]
                left += 1
            elif score > 0:
                if left == right:
                    return score
                power += sortedToks[right]
                score -= 1
                right -= 1
            else: 
                return score
                
        return score
        