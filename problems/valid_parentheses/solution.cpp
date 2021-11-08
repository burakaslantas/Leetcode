class Solution {
public:
    bool isValid(string s) {
        stack<char> mystack;
        
        for( int i = 0; i < s.length(); i++ )
        {
            char c = s[i];
            cout << c;
            if( s[i] == ')' || s[i] == ']' || s[i] == '}' )
            {
                if( mystack.empty() ) return false;
                if( mystack.top() == '(' && s[i] != ')' ) return false;
                if( mystack.top() == '[' && s[i] != ']' ) return false;
                if( mystack.top() == '{' && s[i] != '}' ) return false;
                mystack.pop();
            }
            else
            {
                mystack.push(s[i]);
            }
        }
        
        return mystack.empty();
    }
};
