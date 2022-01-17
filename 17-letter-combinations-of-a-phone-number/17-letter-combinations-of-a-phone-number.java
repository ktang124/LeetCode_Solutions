class Solution {
    public List<String> letterCombinations(String digits) {
        
        List<String> combos = new ArrayList<>();
        if(digits.length() == 0) return combos;
        StringBuffer sBuff = new StringBuffer();
        String[] map = new String[]{"abc","def","ghi","jkl","mno",
"pqrs","tuv","wxyz"};
        dfs(digits, combos, sBuff, map ,0);
        return combos;
    }
    
    private void dfs(String digits, List<String> combos, StringBuffer sBuff, String[] map, int index){
        if(sBuff.length() == digits.length()){
            combos.add(new String(sBuff));
            return;
        }
        int d = digits.charAt(index) - '0';
        String cur = map[d-2];
        for(int i = 0; i < cur.length(); i++){
            sBuff.append(cur.charAt(i));
            dfs(digits, combos, sBuff, map, index+1);
            sBuff.deleteCharAt(sBuff.length()-1);
        }
    }
}