class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> hm = new HashMap<>();
        for(String word : words){
            int num = hm.getOrDefault(word, 0) + 1;
            hm.put(word, num);
        }
        PriorityQueue<String> pq = new PriorityQueue<>((o1, o2) -> hm.get(o2) == hm.get(o1) ? o1.compareTo(o2): hm.get(o2) - hm.get(o1));
                                                
        List<String> res = new ArrayList<>();
        for(String key: hm.keySet()){
            pq.add(key);
        }
        for(int i = 0; i < k; i++){
            res.add(pq.poll());
        }
            
        return res;
    }
}