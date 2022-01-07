class Solution {
    public int search(int[] nums, int target) {
        int offset = 0;
        for(int i = 1; (i < nums.length) && offset == 0; i++){
            if(nums[i-1] > nums[i]){
                offset = i;
            }
        }
        int[] arr = new int[nums.length];
        for(int i = 0; i < nums.length;i++){
            arr[i] = nums[(i+offset)%nums.length];
        }
        
        int left = 0;
        int right = nums.length-1;
        int mid = -1;
     
        while(left <= right){
            mid = left + (right-left)/2;
            if(arr[mid] == target){
                return (mid+offset)%nums.length;
            }else if(arr[mid] > target){
                right = mid-1;
            }else{
                left = mid+1;
            }
        }

        return -1;
    }
}