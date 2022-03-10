class LRUCache

=begin
    :type capacity: Integer
=end
    def initialize(capacity)
        # define global variable @capacity inside this class
        @capacity = capacity
        # define gloable cache as a Hash.new object
        # ruby hash maintains the orderof insertion
        @cache = Hash.new
    end


=begin
    :type key: Integer
    :rtype: Integer
=end
    def get(key)
        val = @cache.delete(key)
        @cache[key] = val if val 
        return val || -1
    end


=begin
    :type key: Integer
    :type value: Integer
    :rtype: Void
=end
    def put(key, value)
        @cache.delete(key)
        @cache[key] = value
        # delete cache's 1st key
        @cache.delete @cache.keys[0] if @cache.size > @capacity
    end

end

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache.new(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)