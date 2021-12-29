class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length == 0) return 0;
        Arrays.sort(nums);
        int longest = 1;
        int localLongest = 1;
        int prev = nums[0];
        for(int i = 1; i < nums.length; i++){
            if(nums[i] - prev == 1){
                localLongest++;
                longest = Math.max(localLongest,longest);
            }else if(nums[i] !=prev){
               localLongest = 1;
            }
            prev = nums[i];
        }
        return longest;
    }
}