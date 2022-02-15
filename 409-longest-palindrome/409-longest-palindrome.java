class Solution {
    public int longestPalindrome(String s) {
        int[] map = new int[128];
        for(char a : s.toCharArray()){
            map[a] += 1;
        }
        boolean hasOdd = false;
        int total = 0;
        for(int m : map){
            if(m % 2 == 0)
                total += m;
            else{
                hasOdd = true;
                total += m -1;
            }
               
            
           
        }
        if(hasOdd) total += 1;
        return total;
    }
}