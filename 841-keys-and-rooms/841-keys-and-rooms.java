class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        boolean[] visited =  new boolean[rooms.size()];
        
        Deque<Integer> visiting = new ArrayDeque<>();
        visiting.push(0);
        while(!visiting.isEmpty()){
            int curIndex = visiting.pollLast();
            List<Integer> room = rooms.get(curIndex);
            for(int key : room){
                if(!visited[key]) visiting.push(key);
            }
            visited[curIndex] = true;
        }
        
        for(int i = 0; i < visited.length; i++){
            if(!visited[i]) return false;
        }
        return true;
            
        
        
    }
    
}