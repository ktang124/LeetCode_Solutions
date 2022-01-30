# @param {Integer} num_rows
# @return {Integer[][]}
def generate(num_rows)
    res = Array.new(num_rows)
    for row in 0..num_rows-1 do
        res[row] = Array.new(row+1)
        res[row][0] = 1
        res[row][row] = 1
    end
    for row in 0..num_rows-1 do
        for col in 0..res[row].length-1 do
            if res[row][col] == nil then
                res[row][col] = res[row-1][col-1] + res[row-1][col]
            end
        end
    end
    res
end