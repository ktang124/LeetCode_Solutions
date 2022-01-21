class Solution {
    public String longestPalindrome(String s) {
        String max = "";
        for(int i = 0; i < s.length(); i ++){
            String palin = expand(s,i);
            if(palin.length() > max.length()){
                max = palin;
            }
        }
        return max;
    }
    
    private String expand(String s, int index){
        int left = index - 1;
        int right = index + 1;
        int len = 0;
        int minLeft;
        int maxRight;
        while(left >= 0 && right < s.length() && (s.charAt(left) == s.charAt(right))){
            left--;
            right++;
        }
        len = right - left;
        minLeft = left;
        maxRight = right;
        
        left = index - 1;
        right = index;
        while(left >= 0 && right < s.length() && (s.charAt(left) == s.charAt(right))){
            left--;
            right++;
        }
        if((right - left) > len){
            minLeft = left;
            maxRight = right;
        }
        
        return s.substring(minLeft+1, maxRight);
    }
}