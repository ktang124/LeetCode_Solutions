class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = [0] * (len(matrix) * len(matrix[0]))
        i = 0
        for row, lst in enumerate(matrix):
            for col, num in enumerate(lst):
                heap[i] = num
                i+=1
                
        heapq.heapify(heap)
        for i in range(k-1):
            heapq.heappop(heap)
            
        return heapq.heappop(heap)