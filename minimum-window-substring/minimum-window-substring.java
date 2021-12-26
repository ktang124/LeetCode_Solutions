class Solution {
    public String minWindow(String s, String t) {
        int[] charMap = new int[128];
        int[] tMap = new int[128];
        if(t.length() > s.length()) return "";
        for(int i = 0; i < t.length(); i++){
            tMap[t.charAt(i)] += 1;
        }
        int l = -1;
        int r = -1;
        int winLen = 99999999;
        
        int start = 0;
        for(int end = 0; end < s.length(); end++){
            char cur = s.charAt(end);
            charMap[cur] += 1;
            while(compare(charMap, tMap)){
                if((end - start + 1) < winLen){
                    l = start;
                    r = end;
                    winLen = (end - start + 1); 
                }
                charMap[s.charAt(start)] -= 1;
                start++;
            }
        }
        if(l == -1 && r == -1) return "";
        return s.substring(l, r+1);
    }
    private boolean compare(int[] a, int[] b){
        for(int i = 0; i < 128; i++){
            if(a[i] < b[i]) return false;
        }
        return true;
    }
}