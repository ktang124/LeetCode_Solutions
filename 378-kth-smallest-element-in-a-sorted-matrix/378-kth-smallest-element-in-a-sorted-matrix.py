class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = [999999999] * (len(matrix) * len(matrix[0]))
        i = 0
        colLen = min(k, len(matrix[0]))
        for row, lst in enumerate(matrix):
            for col in range(colLen):
                heap[i] = lst[col]
                i+=1
                
        heapq.heapify(heap)
        for i in range(k-1):
            heapq.heappop(heap)
            
        return heapq.heappop(heap)