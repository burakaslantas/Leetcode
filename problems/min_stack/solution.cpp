class MinStack {
public:
    void push(int val) {
        mainStack.push(val);
        if( minStack.empty() || val <= minStack.top() ) minStack.push(val);
    }
    
    void pop() {
        if( mainStack.top() == getMin() ) minStack.pop();
        mainStack.pop();
    }
    
    int top() {
        return mainStack.top();
    }
    
    int getMin() {
        return minStack.top();
    }
private:
    stack<int> mainStack;
    stack<int> minStack;
    /*
    struct StackNode {
        int val;
        StackNode* next;
    };
    StackNode* topPtr;
    */
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
