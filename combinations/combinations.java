class Solution {
    public List<List<Integer>> combine(int n, int k) {
        boolean[] visited = new boolean[n];
        List<List<Integer>> combos = new ArrayList<>();
        dfs(visited, k, new ArrayList<>(), combos,0);
        return combos;
    }
    private void dfs(boolean[] visited, int k, List<Integer> combo, List<List<Integer>> combos, int start){
        if(combo.size() == k){
            combos.add(new ArrayList<>(combo));
        }
        for(int i = start; i < visited.length; i++){
            if(!visited[i]){
                visited[i] = true;
                combo.add(i+1);
                dfs(visited, k, combo, combos,i+1);
                visited[i] = false;
                combo.remove(combo.size()-1);
            }
        }
    }
}