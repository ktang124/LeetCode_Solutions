# @param {String} s
# @return {Integer}
def first_uniq_char(s)
    charCount = Hash.new(0)
    for i in 0..s.length-1 do
        curCount = charCount[s[i]]
        charCount[s[i]] = curCount + 1
    end
    for i in 0..s.length-1 do
        if charCount[s[i]] == 1 then
            return i;
        end
    end
    -1
end