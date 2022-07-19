class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = list()
        res.append(list())
        res[0].append(1)
        for row in range(1,numRows):
            res.append(list())
            res[row].append(1)
            for col in range(1,row+1):
                if col == row:
                    res[row].append(1)
                else:
                    res[row].append(res[row-1][col] + res[row-1][col-1])
        return res
                
        