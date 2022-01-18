class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if(strs==null || strs.length==0) return new ArrayList<>();
        Map<String,List<String>> map = new HashMap<>();
        // for each string: 1. using char[] store s.toCharArray(),  sort the char array, convert it to string (String.valueOf(ca)), use if as key
        // 2. arr = new char[26]
        for(String s:strs){
            // char[] arr = new char[26];
            // for(char c:s.toCharArray()){
            //     arr[c-'a']++;
            // }
             //String key = String.valueOf(arr);
            
            char[] charArr = s.toCharArray();
            Arrays.sort(charArr);
            String key = String.valueOf(charArr);
          
            if(!map.containsKey(key)) map.put(key,new ArrayList<>());
            map.get(key).add(s);
        }
        return new ArrayList(map.values());
    }
}