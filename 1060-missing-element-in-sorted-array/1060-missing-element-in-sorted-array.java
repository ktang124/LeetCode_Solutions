class Solution {
    public int missingElement(int[] nums, int k) {
       
        int max = nums[nums.length-1];
        for(int i = 1; i < nums.length; i++){
            k -= (nums[i]-(nums[i-1]+1));
            if(k <= 0){
                return nums[i]-1+k;
            }
        }
        return max + k;
    }
}