class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(lambda: 0)
        for n in nums:
            counts[n] += 1
            
        #sort all the keys by greatest to least by count
        sortList = sorted(counts.keys(), key = lambda x: counts[x], reverse = True)
        return sortList[:k]