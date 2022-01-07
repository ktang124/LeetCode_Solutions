class RandomizedSet {
    HashSet<Integer> rando;
    public RandomizedSet() {
        rando = new HashSet<>();
    }
    
    public boolean insert(int val) {
        return rando.add(val);
        
    }
    
    public boolean remove(int val) {
        return rando.remove(val);
    }
    
    public int getRandom() {
        int r = (int)(Math.random() * rando.size());
        Iterator<Integer> iter = rando.iterator();
        int res = iter.next();
        for(int i = 0; i < r; i++){
            res = iter.next();
        }
        return res;
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */