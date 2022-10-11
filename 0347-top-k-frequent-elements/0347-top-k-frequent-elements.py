class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		counts = Counter(nums)
		sortedKeys = sorted(counts.keys(), key = lambda x: counts[x], reverse = True)
		return sortedKeys[:k]