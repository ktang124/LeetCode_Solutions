class Solution {
    public int numEquivDominoPairs(int[][] dominoes) {
        int equivs = 0;
        Map<Set<Integer>, Integer> pairs = new HashMap<>();
        for(int [] domino : dominoes){
            Set<Integer> d = new HashSet<>();
            d.add(domino[0]);
            d.add(domino[1]);
            int get = pairs.getOrDefault(d, 0);
            equivs += get;
            pairs.put(d, get+1);
     
        }
        return equivs;
    }
}