class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        #find the set of elements of each row in mat
        #then find the intersection of those elements
        listSets = [set(x) for x in mat]
        intersect = listSets[0]
        for lS in listSets[1:]:
            intersect = lS.intersection(intersect)
        if len(intersect) == 0:
            return -1
        return (min(list(intersect)))
    