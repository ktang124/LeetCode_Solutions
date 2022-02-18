class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        Set<String> dnaSet = new HashSet<>();
         Set<String> filter = new HashSet<>();
        
         for(int i = 0; i < s.length()-9; i++){
             String cur = s.substring(i, i + 10);
             if(dnaSet.contains(cur)){
                 if(!filter.contains(cur)) 
                     filter.add(cur);
             }
            dnaSet.add(cur);
         }
        return new ArrayList<>(filter);
    }
}