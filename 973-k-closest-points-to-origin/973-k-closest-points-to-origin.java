class Solution {
    public int[][] kClosest(int[][] points, int k) {
        int[][] res = new int[k][2];
        int[][] map = new int[points.length][3];
        //format is x,y, x^2+y^2
        for(int row = 0; row < points.length; row++){
            int x = points[row][0];
            int y = points[row][1];
            map[row][0] = x*x + y*y;
            map[row][1] = x;
            map[row][2] = y;
        }
        Arrays.sort(map, (o1,o2)-> o1[0] - o2[0]);
        
        for(int i = 0; i < res.length; i++){
            res[i][0] = map[i][1];
            res[i][1] = map[i][2];
        }
        return res;
    }
}