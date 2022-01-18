class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<Map<Character, Integer>, List<String>> hm = new HashMap<>();
        for(String s : strs){
            Map<Character, Integer> map = new HashMap<>();
            for(int i = 0; i < s.length();i++){
               Integer g = map.getOrDefault(s.charAt(i), 0);
                g += 1;
                map.put(s.charAt(i), g);
            }
            List<String> get = hm.getOrDefault(map, new LinkedList<>());
            get.add(s);
            hm.put(map, get);
        }
        List<List<String>> groups = new ArrayList<>(hm.size());
        for(Map<Character, Integer> key : hm.keySet()){
            groups.add(hm.get(key));
        }
        return groups;
    }
}