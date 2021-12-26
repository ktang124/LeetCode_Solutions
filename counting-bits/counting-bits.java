class Solution {
    public int[] countBits(int n) {
        int[] res = new int[n+1];
        for(int i = 0; i < n + 1; i++){
            int count = 0;
            int shift = i;
            for(int j = 0; j < 32; j++){
                if((shift & 1) == 1) count++;
                shift = shift >> 1;
            }
            res[i] = count;
        }
        return res;
    }
}