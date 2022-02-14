class Solution {
    public int lengthOfLongestSubstring(String s) {
        int[] map = new int[128]; //Every ascii value
        int len = 0;
        int start = 0;
        for(int end = 0; end < s.length(); end++){
            map[s.charAt(end)] += 1;
            while(!validMap(map)){ 
                map[s.charAt(start)] -= 1;
                start++;
            }
            len = Math.max(len, end - start + 1);
        }
        return len;
    }
    private boolean validMap(int[] map){
        for(int i = 0; i < map.length; i++){
            if(map[i] > 1){
                return false;
            }
        }
        return true;
    }
}