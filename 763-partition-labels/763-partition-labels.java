class Solution {
    public List<Integer> partitionLabels(String s) {
        List<Integer> partitions = new ArrayList<>();
      
        int[] map = new int[26];
        for(int i = 0; i < s.length(); i++){
            int curChar = s.charAt(i) - 'a';
            map[curChar] = i;
        }
   
        int last = 0;
        int start = 0;
        for(int i = 0; i < s.length(); i++){
            last = Math.max(last, map[s.charAt(i)-'a']);
            if(last == i){
                partitions.add(last - start + 1);
                start = last + 1;
            }
        }
        return partitions;
    }
}