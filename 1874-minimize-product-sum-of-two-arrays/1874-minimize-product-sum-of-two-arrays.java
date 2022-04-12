class Solution {
    public int minProductSum(int[] nums1, int[] nums2) {
        //[1,2,4,5,7]
        //[8,6,4,3,2]
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        int prod = 0;
        int n = nums1.length;
        for(int i = 0; i < n; i++){
            prod += nums1[i]*nums2[n-i-1];
        }
        return prod;
    }
}