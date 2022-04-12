class Solution {
    public int minProductSum(int[] nums1, int[] nums2) {
        //[1,2,4,5,7]
        //[8,6,4,3,2]
        sort(nums1);
        sort(nums2);
        int prod = 0;
        int n = nums1.length;
        for(int i = 0; i < n; i++){
            prod += nums1[i]*nums2[n-i-1];
        }
        return prod;
    }
    private void sort(int[] nums){
        int[] map = new int[100];
        for(int i = 0; i < nums.length; i++){
            map[nums[i]-1] += 1;
        }
        int index = 0;
        for(int i = 0; i < 100; i++){
            for(int j = 0; j < map[i]; j++){
                nums[index++] = i+1;
            }
        }
    }
}