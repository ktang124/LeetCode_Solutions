class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        
        int subSum = 0;
        int minLen = Integer.MAX_VALUE;
        int start = 0;
        for(int end = 0; end < nums.length; end++){
            subSum += nums[end];
            while(subSum >= target){
                minLen = Math.min(minLen, (end-start+1));
                subSum -= nums[start++];
            }
        }
        if(minLen == Integer.MAX_VALUE) return 0;
        return minLen;
    }
}