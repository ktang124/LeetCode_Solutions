class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] prefix = new int[n];
        prefix[0] = nums[0];
        
        for(int i = 1; i < n; i++){
            prefix[i] = prefix[i-1] * nums[i];
        }
        int suffix = 1;
        
        for(int i = n-1; i >= 1; i--){
            prefix[i] = prefix[i-1] * suffix;
            suffix *= nums[i];
        }
        prefix[0] = suffix;
        
        return prefix;
    }
}