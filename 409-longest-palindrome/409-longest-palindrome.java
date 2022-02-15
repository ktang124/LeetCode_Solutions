class Solution {
    public int longestPalindrome(String s) {
        int[] map = new int[128];
        for(char a : s.toCharArray()){
            map[a] += 1;
        }
        boolean hasOdd = false;
        int total = 0;
        for(int m : map){
           total += (m/2 * 2);   
        }
        if(total < s.length()) total++;
        return total;
    }
}