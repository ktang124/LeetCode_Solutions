class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        
        List<List<Integer>> result = new ArrayList<>();
        
        backtrack(result, nums, 0);
        
        return result;
    }
    
    public void backtrack(List<List<Integer>> result, int[] nums, int start){
        if(start == nums.length){
            result.add(toList(nums));  //also convert array to list
        }
        else{
            for(int i = start; i < nums.length; i++){
                
                //to check for duplicates
                if(i != start && !canPermutate(start, i, nums)) continue;
                //this method will check if number start has appeared before in list of nums
                
                swap(i, start, nums);
                backtrack(result, nums, start + 1);
                swap(i, start, nums);   //to bring it to initial position
            }
        }
    }
    
    //to convert nums array to list
    public List<Integer> toList(int[] nums){
        List<Integer> res = new ArrayList<>();
        for(int i : nums)
            res.add(i);
        
        return res;
    }
    
    public void swap(int i, int j, int[] nums){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    
    public boolean canPermutate(int start, int curr, int[] nums){
        for(int i = start; i < curr; i++){
            if(nums[i] == nums[curr]){
                return false;
            }
        }
        return true;
    }
}

//SC = O(1)
//TC = O(N!)