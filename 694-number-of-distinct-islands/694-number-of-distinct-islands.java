class Solution {
    public int numDistinctIslands(int[][] grid) {
        //they have to be not the same shape
        Map<Pair<Integer,Integer>, Set<Pair<Integer,Integer>>> hm = new HashMap<>();
        for(int row = 0; row < grid.length; row++){
            for(int col = 0; col < grid[0].length; col++){
                if(grid[row][col] == 1){
                    dfs(row, col, grid, row, col, hm);
                }
            }
        }
        Set<Set<Pair<Integer,Integer>>> hs = new HashSet<>();
        for(Pair<Integer,Integer> key : hm.keySet()){
            hs.add(hm.get(key));
        }
        return hs.size();
    }
    private void dfs(int row, int col, int[][] grid, int origRow, int origCol, Map<Pair<Integer,Integer>, Set<Pair<Integer,Integer>>> hm){
        if(row < 0 || col < 0 || row >= grid.length || col >= grid[0].length || grid[row][col] == 0){
            return;
        }
        Pair<Integer, Integer> coord = new Pair<>(origRow, origCol);
        Set<Pair<Integer,Integer>> cur = hm.getOrDefault(coord, new HashSet<>());
        cur.add(new Pair<>(row-origRow, col - origCol));
        hm.put(coord,cur);
        grid[row][col] = 0;
        dfs(row-1, col, grid, origRow, origCol, hm);
        dfs(row+1, col, grid, origRow, origCol, hm);
        dfs(row, col-1, grid, origRow, origCol, hm);
        dfs(row, col+1, grid, origRow, origCol, hm);
    }
}