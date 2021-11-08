class MyQueue {
public:
    void push(int x) {
        s1.push(x);
    }
    
    int pop() {
        int result;
        
        while( !s1.empty() )
        {
            int temp = s1.top();
            s1.pop();
            s2.push(temp);
        }
        
        result = s2.top();
        s2.pop();
        
        while( !s2.empty() )
        {
            int temp = s2.top();
            s2.pop();
            s1.push(temp);
        }
        
        return result;
    }
    
    int peek() {
        int result;
        
        while( !s1.empty() )
        {
            int temp = s1.top();
            s1.pop();
            s2.push(temp);
        }
        
        result = s2.top();
        
        while( !s2.empty() )
        {
            int temp = s2.top();
            s2.pop();
            s1.push(temp);
        }
        
        return result;
    }
    
    bool empty() {
        return s1.empty() && s2.empty();
    }
private:
    stack<int> s1;
    stack<int> s2;
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
