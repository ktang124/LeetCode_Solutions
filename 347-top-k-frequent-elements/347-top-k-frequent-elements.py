class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        #sort all the keys by greatest to least by count
        sortList = sorted(counts.keys(), key = lambda x: counts[x], reverse = True)
        return sortList[:k]