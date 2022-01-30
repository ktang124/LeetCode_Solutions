# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
    min = 99999
    maxProf = 0
  
    for i in 0..prices.length-1 do
        if prices[i] < min then 
            min = prices[i]
        end
        if prices[i] - min > maxProf then
            maxProf = prices[i] - min
        end
    end
    maxProf
end