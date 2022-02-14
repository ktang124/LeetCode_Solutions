class Solution {
    public int lengthOfLongestSubstring(String s) {
        int[] map = new int[128]; //Every ascii value
        int len = 0;
        int start = 0;
        int numOver = 0;
        for(int end = 0; end < s.length(); end++){
            map[s.charAt(end)] += 1;
            if(map[s.charAt(end)] == 2) numOver+=1;
            while(numOver > 0){ 
                if(map[s.charAt(start)] == 2) numOver-=1;
                map[s.charAt(start)] -= 1;
                start++;
            }
            len = Math.max(len, end - start + 1);
        }
        return len;
    }
    
}