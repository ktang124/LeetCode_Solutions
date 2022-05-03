class Solution {
    public String customSortString(String order, String s) {
        Map<Character, Integer> pos = new HashMap<>();
        
        for(int i = 0; i < order.length(); i++){
            char cur = order.charAt(i);
            pos.put(cur, i);
        }
        
      PriorityQueue<Character> pq = new PriorityQueue<>((o1, o2) -> pos.getOrDefault(o1, 28) - pos.getOrDefault(o2, 28));
        for(char c : s.toCharArray()){
            pq.add(c);
        }
        StringBuffer buff = new StringBuffer();
        while(!pq.isEmpty()){
            buff.append(pq.poll());
        }
     
        return new String(buff);
    }
}