class Solution {
    public int rob(int[] nums) {
        if(nums.length == 1){
            return nums[0];
        }
        int[] dpFirst = new int[nums.length+1];
        int[] dpSecond = new int[nums.length+1];
        
        dpFirst[0] = 0;
        dpFirst[1] = nums[0];
        dpSecond[0] = 0;
        dpSecond[1] = 0;
        
        for(int i = 1; i < nums.length; i++){
            dpFirst[i+1] = Math.max(nums[i] + dpFirst[i-1],dpFirst[i]);
            dpSecond[i+1] = Math.max(nums[i] + dpSecond[i-1], dpSecond[i]);
        }
        
        return Math.max(dpFirst[nums.length-1], dpSecond[nums.length]);
    }
}