class Solution:
    def topKFrequent(self, nums, k):
        #make buckets of each frequency, an element can appear at most k times
        bucket = [[] for _ in range(len(nums) + 1)]
        #make a counter of the items
        Count = Counter(nums)  
        for num, freq in Count.items():
            bucket[freq].append(num) 
        
        flat_list = []
        for b in bucket:
            for item in b:
                flat_list.append(item)
        return flat_list[len(flat_list)-k:]