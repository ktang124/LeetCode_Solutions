class MinStack {
    Deque<Integer> stack;
    PriorityQueue<Integer> minStack;
    public MinStack() {
        stack = new ArrayDeque<>();
        minStack = new PriorityQueue<>();
    }
    
    public void push(int val) {
        stack.push(val);
        minStack.add(val);
    }
    
    public void pop() {
        int remove = stack.pop();
        minStack.remove(remove);
    }
    
    public int top() {
        return stack.peek();        
    }
    
    public int getMin() {
        return minStack.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */