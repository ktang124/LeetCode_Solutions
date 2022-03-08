class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        Map<Integer, Set<Integer>> courses = new HashMap<>();
        int[] order = new int[numCourses];
       
        int[] preReqNum = new int[numCourses];
        /*make the graph and count the preReqNum of each course*/
        for(int[] req : prerequisites){
            int canTake = req[1];
            int cannotTake = req[0];
            Set<Integer> preFor = courses.getOrDefault(canTake, new HashSet<>());
            preFor.add(cannotTake);
            preReqNum[cannotTake] += 1;
            courses.put(canTake, preFor);
        }
        
        int index = 0;
        /*add all of the courses that have no prerequisites into the queue*/
        Deque<Integer> dq = new ArrayDeque<>();
        for(int i = 0; i < numCourses;i++){
            if((preReqNum[i] == 0)){
                order[index++] = i;
                dq.addFirst(i);
            }
        }
         /* kahn's algorithm*/
        while(!dq.isEmpty()){
            int check = dq.pollLast();
            Set<Integer> cannotTake = courses.getOrDefault(check, new HashSet<>());
            for(int key : cannotTake){
                preReqNum[key] -= 1;
                if(preReqNum[key] == 0){
                    order[index++] = key;
                    dq.addFirst(key);
                }
            }
        }
        /*this means a cycle was detected and not all nodes were added to the ordering*/
        if(index != numCourses){
            return new int[0];
        }
        return order;
        }
}