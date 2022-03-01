class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> hm = new HashMap<>();
        for(int num : nums){
            int count = hm.getOrDefault(num, 0) + 1;
            hm.put(num, count);
        }
        
        int[] res = new int[k];
        int index = 0;
        for(int i = 0; i < k; i++){
            int max = -1;
            int maxKey = 0;
            for(int key : hm.keySet()){
                if(hm.get(key) > max){
                    max = hm.get(key);
                    maxKey = key;
                }
            }
            res[index] = maxKey;
            hm.put(maxKey, -2);
            index++;
        }
        return res;
    }
}