class BrowserHistory {
    Deque<String> history;
    Deque<String> forward;
    
    public BrowserHistory(String homepage) {
        history = new ArrayDeque<>();
        forward = new ArrayDeque<>();
        history.push(homepage);
        
        
    }
    
    public void visit(String url) {
        history.push(url);
        forward = new ArrayDeque<>();
    }
    
    public String back(int steps) {
        while (steps > 0 && history.size() > 1){
            String popped = history.pop();
            forward.push(popped);
            steps -= 1;
        }
        return history.peek();
        
    }
    
    public String forward(int steps) {
        while(steps > 0 && forward.size() > 0){
            String popped = forward.pop();
            history.push(popped);
            steps -= 1;
        }
        return history.peek();
    }
}
//leetcode.com, google.com, facebook.com,youtube.com
/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory obj = new BrowserHistory(homepage);
 * obj.visit(url);
 * String param_2 = obj.back(steps);
 * String param_3 = obj.forward(steps);
 */