class MyHashMap {
    boolean[] on = new boolean[1000001];
    int[] val = new int[1000001];
    /** Initialize your data structure here. */
    public MyHashMap() {
        
    }
    
    /** value will always be non-negative. */
    public void put(int key, int value) {
        on[key] = true;
        val[key] = value;
    }
    
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    public int get(int key) {
        if (on[key]) return val[key];
        return -1;
    }
    
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    public void remove(int key) {
        on[key] = false;
    }
}