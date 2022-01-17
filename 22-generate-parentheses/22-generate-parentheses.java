class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> parens = new ArrayList<>();
        if(n == 0) return parens;
        dfs(n, parens, new StringBuffer(), 0,0);
        return parens;
    }
    private void dfs(int n, List<String> parens, StringBuffer sBuff, int left, int right){
       
        if(sBuff.length() == (n*2)){
            parens.add(new String(sBuff));
            return;
        }
        if(left < n){
       sBuff.append('(');
        dfs(n, parens, sBuff, left+1, right);
        sBuff.deleteCharAt(sBuff.length()-1);
        }
        if(right < left){
         sBuff.append(')');
        dfs(n, parens, sBuff, left, right+1);
        sBuff.deleteCharAt(sBuff.length()-1);
        }
    }
}