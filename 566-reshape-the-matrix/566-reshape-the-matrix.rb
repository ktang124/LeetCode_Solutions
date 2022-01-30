# @param {Integer[][]} mat
# @param {Integer} r
# @param {Integer} c
# @return {Integer[][]}
def matrix_reshape(mat, r, c)
    if mat.length * mat[0].length != r * c then
        return mat;
    end
    res = Array.new(r){Array.new(c)}
    rIndex = 0
    cIndex = 0
    for row in 0..mat.length-1
        for col in 0..mat[0].length-1
           
            res[rIndex][cIndex] = mat[row][col]
            cIndex += 1
            if cIndex == c then
                rIndex+= 1
                cIndex = 0
            end
        end
    end
    res
end