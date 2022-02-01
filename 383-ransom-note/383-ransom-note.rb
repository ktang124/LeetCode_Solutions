def can_construct(ransom_note, magazine)
    note_hash = Hash.new(0)
    magazine_hash =Hash.new(0)
    
    ransom_note.each_char do |char|
        note_hash[char] +=1
    end
    magazine.each_char do |char|
       magazine_hash[char] +=1
    end
    note_hash.keys.each do |key|
        return false if note_hash[key]>magazine_hash[key]
    end
    true
end