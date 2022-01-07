class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int top = 0;
        int bottom = matrix.length;
        int left = 0;
        int right = matrix[0].length;
        int mid = matRow(matrix, target);
        if(mid == -1) return false;
        int[] r = matrix[mid];
        int m = 0;
        while(left <= right){
            m = left + (right-left)/2;
            if(r[m] == target){
                return true;
            }else if(r[m] < target){
                left = m+1;
            }else if(r[m] > target){
                right = m-1;
            }
        }
        return false;
        
    }
    private int matRow(int[][] matrix, int target){
        int top = 0;
        int bottom = matrix.length-1;
        int len = matrix[0].length-1;
        while(top <= bottom){
            int mid = top + (bottom-top)/2;
            if(matrix[mid][0] <= target && target <= matrix[mid][len]){
                return mid;
            }else if(target < matrix[mid][0]){
                bottom = mid-1;
            }else if(target > matrix[mid][0]){
               top = mid+1;
            }
        }
        return -1;
    }
}