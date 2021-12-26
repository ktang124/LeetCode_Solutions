class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Set<List<Integer>> resSet = new HashSet<>();
      
        if(candidates.length == 0) return new ArrayList<>();
        Arrays.sort(candidates);
        dfs(candidates, target, resSet, new ArrayList<Integer>(), 0);
        return new ArrayList<>(resSet);
    }
    private void dfs(int[] candidates, int target, Set<List<Integer>> resSet, List<Integer> lst, int start){
        if(target < 0){
            return;
        }
        if(target == 0){
            resSet.add(new ArrayList<>(lst));
        }
        for(int i = start; i < candidates.length; i++){
            lst.add(candidates[i]);
            dfs(candidates, target - candidates[i], resSet, lst, i);
            lst.remove(lst.size()-1);
        }
    }
}