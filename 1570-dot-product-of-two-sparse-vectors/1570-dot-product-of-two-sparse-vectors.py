class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.vector[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        keys = set.intersection(set(self.vector.keys()), set(vec.vector.keys()))
        return sum([self.vector[i] * vec.vector[i] for i in keys])
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)