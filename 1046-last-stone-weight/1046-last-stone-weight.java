class Solution {
    public int lastStoneWeight(int[] stones) {
        
        PriorityQueue<Integer> maxPq = new PriorityQueue<>(Collections.reverseOrder());
        for(int stone : stones){
            maxPq.add(stone);
        }
        //[1,1,2,4,1,8]
       while(maxPq.size() > 1){
            int y = maxPq.poll();
           int x = maxPq.poll();
           if((y-x) != 0 ) maxPq.add(y-x);
       }
      if(maxPq.isEmpty()) return 0;
        return maxPq.poll();
    }
}