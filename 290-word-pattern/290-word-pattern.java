class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] arr = s.split(" ");
        Map<Character, String> hm = new HashMap<>();
        Set<String> used = new HashSet<>();
        int i = 0;
        for(String a : arr){
            if(i== pattern.length()) return false;
            char cur = pattern.charAt(i);
            i++;
            if(!hm.containsKey(cur)){
                if(used.contains(a)) 
                    return false;
                else{
                    hm.put(cur, a);
                    used.add(a);
                }
            }else{
                if(!(hm.get(cur).equals(a))) return false;
            }
           
        }
       return (i == pattern.length());

    }
}