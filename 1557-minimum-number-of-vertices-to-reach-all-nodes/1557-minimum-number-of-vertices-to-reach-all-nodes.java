class Solution {
    public List<Integer> findSmallestSetOfVertices(int n, List<List<Integer>> edges) {
        List<Integer> res = new ArrayList<>();
        //topological sort, kahn's algorithm
        boolean[] pointedTo = new boolean[n];
        for(List<Integer> edge : edges){
            pointedTo[edge.get(1)] = true;
        }
        
        for(int i = 0; i < n; i++){
            if(!pointedTo[i]) res.add(i);
        }
        return res;
    }
}