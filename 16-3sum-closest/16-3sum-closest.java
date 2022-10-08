class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int diff = 10000000;
        
        for (int i = 0; i < nums.length; i++) {
            int j = i+1;
            int n = nums.length - 1;
            
            while (j < n) {
                int sum = nums[i] + nums[j] + nums[n];
            
                if (sum == target) 
                    return target;
            
                if (Math.abs(target - sum) < Math.abs(diff)){
                    diff = target-sum;
                }
                
                if ((target - sum) < 0)
                    n--;
                else if((target-sum) > 0) 
                    j++;
            }
        }
        return target-diff;
     
    }
}