/* The knows API is defined in the parent class Relation.
      boolean knows(int a, int b); */

public class Solution extends Relation {
    public int findCelebrity(int n) {
       int[] degree = new int[n];
        int[] numEdges = new int[n];
        //false default, if true, the index number could be celebrity
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(i != j  && knows(i,j)){
                    degree[j] += 1;
                    numEdges[i] += 1;
                }
            }
        }
        for(int i = 0; i < n; i++){
            if((degree[i] == n-1) && numEdges[i] == 0) return i;
        }
        return -1;
    }
}