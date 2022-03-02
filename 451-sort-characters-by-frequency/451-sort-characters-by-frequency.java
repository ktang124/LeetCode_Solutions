class Solution {
    public String frequencySort(String s) {
        
        //we make a map of the char ascii value to the number of that char present
        int[][] map = new int[128][2];
        for(int i = 0; i < 128; i++){
            map[i][0] = i;
        }
        for(int i = 0; i < s.length(); i++){
            map[s.charAt(i)][1] += 1;
        }
        
        //we can now sort the array by the descending order of the number of each char
        Arrays.sort(map, (o1, o2) -> (o2[1] - o1[1]));
        
        //we can take advantage of the fact that the result string will only be s.length() so 
        //it is possible to get rid of the overhead of stringbuffer and only use char array
        //to build the result string
        StringBuffer res = new StringBuffer();
        int index = 0;
        for(int i = 0; i < 128; i++){
            int cur = map[i][1];
            for(int j = 0; j < cur; j++){
               res.append((char)(map[i][0]));
            }
        }
        return new String(res);
        
    }
}