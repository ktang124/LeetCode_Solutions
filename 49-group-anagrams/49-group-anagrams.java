class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if(strs==null || strs.length==0) return new ArrayList<>();
        Map<String, List<String>> hm = new HashMap<>();
        
        for(String str : strs){
            char[] sArray = str.toCharArray();
            Arrays.sort(sArray);
            String key = new String(sArray);
            List<String> curList = hm.getOrDefault(key, new ArrayList<>());
            curList.add(str);
            hm.put(key, curList);
        }
        return new ArrayList<>(hm.values());
    }
}