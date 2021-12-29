class Solution {
    public int findComplement(int num) {
        int n = num;
        int zeroes = 0;
        int lead = 0;
        
        for(int i = 0; i < 32; i++){
            if((num & 1) == 0){
                zeroes++;
            }else{
                zeroes = 0;
            }
            num = num >>1;
        }
        int mask = 0;
        int one = 1;
        for(int i =0; i < (32-zeroes); i++){
            mask = mask | one;
            one = one << 1;
        }
        n = n ^ mask;
        return n;
    }
}