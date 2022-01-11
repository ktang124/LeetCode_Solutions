class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        int numArrays = 0;
        int subProduct = 1;
        int start = 0;
        for(int end = 0; end < nums.length;end++){
            subProduct = subProduct * nums[end];
            
            while(start < nums.length && subProduct >= k){
                subProduct /= nums[start];
                start++;
            }
            if(subProduct < k){
                numArrays += end-start+1;
            }
        }
        return numArrays;
    }
}