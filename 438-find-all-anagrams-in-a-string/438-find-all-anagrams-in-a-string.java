class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int[] map = new int[26];
        //make a map of the characters in p
        List<Integer> anagrams = new ArrayList<>();
        char[] pArr = p.toCharArray();
        for(char c : pArr){
            map[c-'a'] += 1;
            //counts characters in p
        }
        
        char[] sArray= s.toCharArray();
        int numLeft = p.length();
        //num of characters needed to make an anagram
        
        int start = 0;
        for(int end = 0; end < sArray.length; end++){
            int index = sArray[end] - 'a';
            //if the character is in p, it will be positive in the map
            if(map[index] > 0) numLeft--;
            map[index] -= 1;
            
            //this while trims off start values
            while(map[index] < 0){
                if(map[sArray[start] - 'a'] >= 0) numLeft++;
                map[sArray[start] - 'a'] += 1;
                start++;
            }
            if(numLeft == 0) anagrams.add(start);
        }
        return anagrams;
    }
}