class Solution {
    public boolean canCross(int[] stones) {
        int units = stones[stones.length-1];
        Map<Integer, Set<Integer>> dp = new HashMap<>();
      
        for(int num : stones){
         
             dp.put(num, new HashSet<>());
        }
       
        dp.get(0).add(0);
        for(int i : stones){
            Set<Integer> ks = dp.get(i);
            for(int k : ks){
               
                for(int jump = k-1; jump <= k+1; jump++){
                    int travel = i+jump;
                    if( jump != 0 && dp.containsKey(travel))
                        dp.get(travel).add(jump);
                }
            }
            
            
        }
        return (dp.get(units).size() > 0);
        
    }
}