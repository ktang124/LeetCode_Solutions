class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        Set<List<Integer>> perms = new HashSet<>();
        Arrays.sort(nums);
        if(nums == null) return new ArrayList<>();
        boolean[] visited = new boolean[nums.length];
        dfs(perms, visited, nums, new ArrayList<>());
        return new ArrayList<>(perms);
    }
    private void dfs(Set<List<Integer>> perms, boolean[] visited, int[] nums, List<Integer> perm){
        if(perm.size() == nums.length){
            perms.add(new ArrayList<>(perm));
            return;
        }
        for(int i = 0; i < nums.length; i++){
            if(!visited[i]){
                visited[i] = true;
                perm.add(nums[i]);
                dfs(perms, visited, nums, perm);
                visited[i] = false;
                perm.remove(perm.size()-1);
            }
        }
    }
}