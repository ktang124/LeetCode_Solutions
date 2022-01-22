class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        boolean[] canMake = new boolean[s.length()+1];
        canMake[0] = true;
        for(int i = 1; i < canMake.length; i++){
            for(String word : wordDict){
                //each word in the dict
                int check = (i - word.length());
                //see if the word in dict matches a portion of s
                if(check >= 0 && canMake[check] && s.substring(check, i).equals(word)){
                    canMake[i] = true;
                }
            }
        }
        return canMake[canMake.length-1];
    }
}