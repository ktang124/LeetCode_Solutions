class Solution:
    def topKFrequent(self, nums, k):
        #make buckets of each frequency, an element can appear at most k times
        bucket = [[] for _ in range(len(nums) + 1)]
        #make a counter of the items
        Count = Counter(nums)  
        for num, freq in Count.items():
            bucket[freq].append(num) 
        flat_list = [item for sublist in bucket for item in sublist]
        return flat_list[len(flat_list)-k:]