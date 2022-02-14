# @param {String} s
# @return {Integer}
def length_of_longest_substring(s)
    map = Hash.new(0)
    start = 0
    numOver = 0
    len = 0
    for right in 0..s.length-1
        map[s[right]] += 1
        if(map[s[right]] == 2) 
            numOver += 1
        end
        while(numOver > 0)
            if(map[s[start]] == 2)
                numOver -= 1
            end
            map[s[start]] -= 1
            start += 1
        end
        len = [len, right - start + 1].max
    end
    len
end