class Solution {
    public int lengthOfLongestSubstring(String s) {
        int longest = 0;
        boolean[] map = new boolean[128];
        
        int start = 0;
        for(int end = 0; end < s.length(); end++){
            char curr = s.charAt(end);
            
            while(map[curr]){
                map[s.charAt(start)] = false;
                start++;
            }
            map[curr] = true;
            longest = Math.max(longest, end - start + 1);   
        }
        return longest;
    }
}