class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        Set<List<Integer>> res = new HashSet<>();
        if(nums.length == 0){
            List<List<Integer>> ret = new ArrayList<>();
            return ret;
        }
        for(int i = 0; i < nums.length; i++){
            int target = -1 * nums[i];
            Map<Integer, Integer> hm = new HashMap<>();
            for(int start = i+1; start < nums.length; start++){
                //nums[start] +  target == -nums[i] 
                int complement = target - nums[start];
                if(hm.containsKey(complement)){
                    List<Integer> toAdd = new ArrayList<>();
                    toAdd.add(nums[i]);
                    toAdd.add(nums[start]);
                    toAdd.add(complement);
                    res.add(toAdd);
                }
                hm.put(nums[start], start);
            }
        }
        List<List<Integer>> ret = new ArrayList<>(res);
        
        return ret;
    }
}