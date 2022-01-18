class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int canPlace = 0;
        
        for(int i = 0; i< flowerbed.length; i++){
            if(flowerbed[i] == 0){
                boolean fBehind = (i==0 || flowerbed[i-1] == 0);
                boolean front = (i == flowerbed.length-1 || flowerbed[i+1] == 0);
                if(fBehind && front){
                    canPlace++;
                    flowerbed[i] = 1;
                }
                   
            }
        }
        return canPlace >= n;
    }
}