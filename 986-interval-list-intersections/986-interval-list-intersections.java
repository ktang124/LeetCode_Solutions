class Solution {
    public int[][] intervalIntersection(int[][] f, int[][] s) {
        List<int[]> res = new ArrayList<>();
        int i = 0;
        int j = 0;
        
        while( i < f.length && j < s.length){
            
            int low = Math.max(f[i][0], s[j][0]);
            int high = Math.min(f[i][1], s[j][1]);
            
            if(low <= high){
                res.add(new int[]{low,high});
            }
            if(f[i][1] < s[j][1]){
                i++;
            }else{
                j++;
            }
        }
        return res.toArray(new int[res.size()][2]);
    }
}