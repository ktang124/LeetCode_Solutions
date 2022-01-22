class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        Arrays.fill(dp,1);
        int max = 1;
        for(int start = 1; start < dp.length; start++){
            for(int back = start; back >= 0; back--){
                if(nums[start] > nums[back]){
                    dp[start] = Math.max(dp[start], dp[back] + 1);
                   
                }
            }
        }
        for(int c : dp){
            max = Math.max(c,max);
        }
        return max;
    }
}