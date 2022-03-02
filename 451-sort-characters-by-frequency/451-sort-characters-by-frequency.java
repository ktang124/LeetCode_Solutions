class Solution {
    public String frequencySort(String s) {
        int[][] map = new int[128][2];
        for(int i = 0; i < 128; i++){
            map[i][0] = i;
        }
        for(int i = 0; i < s.length(); i++){
            map[s.charAt(i)][1] += 1;
        }
        Arrays.sort(map, (o1, o2) -> (o2[1] - o1[1]));
        char[] res = new char[s.length()];
        int index = 0;
        for(int i = 0; i < 128; i++){
            int cur = map[i][1];
            for(int j = 0; j < cur; j++){
                res[index++] = (char)(map[i][0]);
            }
        }
        return new String(res);
        
    }
}