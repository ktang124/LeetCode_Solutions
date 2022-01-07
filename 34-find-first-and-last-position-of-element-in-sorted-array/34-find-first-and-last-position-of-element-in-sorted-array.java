class Solution {
    public int[] searchRange(int[] nums, int target) {
        int left = 0;
        int right = nums.length-1;
        int mid = -1;
        boolean targetFound = false;
        while(left <= right && !targetFound){
            mid = left + (right-left)/2;
            if(target == nums[mid]){
                targetFound = true;
            }else if(target < nums[mid]){
                right = mid-1;
            }else{
                left = mid+1;
            }
        }
        if(!targetFound) return new int[]{-1,-1};
        left = mid;
        right = mid;
        while(left >= 0 && nums[left] == target){
            left--;
        }
        while(right < nums.length && nums[right] == target){
            right++;
        }
        return new int[]{left+1,right-1};
    }
}