# @param {String} s
# @return {Integer}
def first_uniq_char(s)
  result = []
  ("a".."z").each do |letter|
    result << s.index(letter) if s.count(letter) == 1
  end
  result.empty? ? -1 : result.min
end