class Solution {
    public int[][] highFive(int[][] items) {
        
        Map<Integer, List<Integer>> hm = new TreeMap<>();
     
        for(int[] item : items){
            List<Integer> get = hm.getOrDefault(item[0], new ArrayList<>());
            get.add(item[1]);
            hm.put(item[0],get);
        }
        int[][] res = new int[hm.size()][2];
        int index = 0;
         for(int key : hm.keySet()){
             int sum = 0;
            List<Integer> get = hm.get(key);
             Collections.sort(get);
             res[index][0] = key;
             
             for(int i = 0; i < 5; i++){
                 sum += get.get(get.size()-1-i);
             }
             sum/=5;
             res[index][1] = sum;
             index++;
        }
        return res;
    }
}