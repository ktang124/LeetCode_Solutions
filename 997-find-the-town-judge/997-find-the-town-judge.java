class Solution {
    public int findJudge(int n, int[][] trust) {
        int[] judge = new int[n];
        boolean[] notJudge = new boolean[n];
        for(int[] t : trust){
            notJudge[t[0]-1] = true;
            judge[t[1]-1] += 1;
        }
        
        for(int i = 0; i < n; i++){
            if(!notJudge[i] && judge[i] == n-1) return i+1;
        }
        return -1;
    }
}