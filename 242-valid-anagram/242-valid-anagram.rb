# @param {String} s
# @param {String} t
# @return {Boolean}
def is_anagram(s, t)
    s_hash = Hash.new(0)
    t_hash =Hash.new(0)
    
    s.each_char do |char|
        s_hash[char] +=1
    end
    t.each_char do |char|
       t_hash[char] +=1
    end
    s_hash.keys.each do |key|
        return false if s_hash[key] != t_hash[key]
    end
    t_hash.keys.each do |key|
        return false if s_hash[key] != t_hash[key]
    end
    true
end