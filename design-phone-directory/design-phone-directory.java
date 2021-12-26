class PhoneDirectory {
    boolean[] pd;
    Set<Integer> avails;
    int getCalls;
    public PhoneDirectory(int maxNumbers) {
        avails = new HashSet<>();
        for(int i = 0; i < maxNumbers; i++){
            avails.add(i);
        }
    }
    
    public int get() {
        if(avails.size() == 0) return -1;
        int res = avails.iterator().next();
        avails.remove(res);
        return res;
    }
    
    public boolean check(int number) {
        return avails.contains(number);
    }
    
    public void release(int number) {
        avails.add(number);
    }
}

/**
 * Your PhoneDirectory object will be instantiated and called as such:
 * PhoneDirectory obj = new PhoneDirectory(maxNumbers);
 * int param_1 = obj.get();
 * boolean param_2 = obj.check(number);
 * obj.release(number);
 */