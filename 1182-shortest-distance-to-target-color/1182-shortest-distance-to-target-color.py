class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        #easiest way would be to go from every single color and try to find the adjacent color
        #store this info in a lookup table
        lookup = [[0] * len(colors) for i in range(3)]
        #index is by color-1, index lookup
        #index is query[0], query[1]-1
        #use a stack to figure out which indices are closest
        closest = [-1] * 3
        for i, color in enumerate(colors):
            closest[color-1] = i
            lookup[0][i] = closest[0]
            lookup[1][i] = closest[1]
            lookup[2][i] = closest[2]
            
        closest = [-1] * 3
        for i in reversed(range(len(colors))):
            color = colors[i]
            closest[color-1] = i
            lookup[0][i] = closest[0] if lookup[0][i] == -1 or abs(closest[0]-i) < abs(lookup[0][i]-i) else lookup[0][i]
            lookup[1][i] = closest[1] if lookup[1][i] == -1 or abs(closest[1]-i) < abs(lookup[1][i]-i) else lookup[1][i]
            lookup[2][i] = closest[2] if lookup[2][i] == -1 or abs(closest[2]-i) < abs(lookup[2][i]-i) else lookup[2][i]
            
        res = []
        for query in queries:
            c = query[1]-1
            index = query[0]
            if lookup[c][index] == -1:
                res.append(-1)
            else:
                res.append(abs(lookup[c][index]-index))
            
        return res