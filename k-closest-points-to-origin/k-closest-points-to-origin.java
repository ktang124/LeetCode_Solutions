class Solution {
    public int[][] kClosest(int[][] points, int k) {
        int[][] closest = new int[k][2];
        /*return array*/
        
        int[] distances = new int[points.length];
        /*list of distances */
        int i = 0;
        Map<Integer, Set<int[]>> hm = new HashMap<>();
        for(int[] point : points){
            int x = point[0];
            int y = point[1];
            int distance = (x*x) + (y*y);
            distances[i++] = distance;
            Set<int[]> get = hm.getOrDefault(distance, new HashSet<>());
            get.add(point);
            hm.put(distance, get);
        }
        Arrays.sort(distances);
        int index = 0;
        for(int j = 0; (j < k) && (index < k); j++){
            Set<int[]> arrs = hm.get(distances[j]);
            for(int[] arr : arrs){
                if(index >= k) break;
                closest[index][0] = arr[0];
                closest[index][1] = arr[1];
                index++;
            }
           
        }
        return closest;
    }
}