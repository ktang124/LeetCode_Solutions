class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        for(int row = 0; row < matrix.length; row++){
            if(binSearch(matrix[row], target) != -1) return true;
        }
        return false;
    }
    private int binSearch(int[] r, int target){
        int left = 0; 
        int right = r.length-1;
        
        while (left <= right){
            int mid = left + (right-left)/2;
            if(r[mid] == target){
                return mid;
            }else if(r[mid] < target){
                left = mid+1;
            }else{
                right = mid-1;
            }
        }
        return -1;
    }
}