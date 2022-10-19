class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        if k == 0 or words is None:
            return None
        
        buckets = [[] for i in range(len(words))]
        counter = Counter(words)
        for word, count in counter.items():
            buckets[count].append(word)
        res = []
        for i in reversed(range(len(buckets))):
            j = 0
            buckets[i].sort()
            while j < len(buckets[i]) and k > 0:
                res.append(buckets[i][j])
                j+= 1
                k-=1 
        return res