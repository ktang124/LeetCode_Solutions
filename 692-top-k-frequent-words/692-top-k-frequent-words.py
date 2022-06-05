class Count:
    def __init__(self, count, key):
        self.count = count
        self.key = key
    
    def __lt__(self, other):
        
        if self.count == other.count:
            return self.key > other.key
        
        return self.count < other.count

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        if k == 0 or words is None:
            return None
        
        output = deque()
        heap = []
        counts = Counter(words)
        
        for key in counts:
            
            heapq.heappush(heap, Count(counts[key], key))
            
            if len(heap) > k:
                _ = heapq.heappop(heap)
            
        
        while heap:
            curr = heapq.heappop(heap)
            
            output.appendleft(curr.key)
            
        return output