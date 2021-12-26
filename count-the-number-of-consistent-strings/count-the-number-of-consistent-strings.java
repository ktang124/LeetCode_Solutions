class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
       boolean[] letters = new boolean[26]; 
        for(int i = 0; i < allowed.length(); i++){
            letters[allowed.charAt(i) -'a'] = true;
        }
        int consistent = 0;
        for(String word : words){
            boolean isConsistent = true;
            for(int i = 0; (i < word.length() && isConsistent); i++){
                if(letters[word.charAt(i)-'a'] == false) isConsistent = false;
            }
            if(isConsistent) consistent++;
        }
        return consistent;
    }
}