class Solution {
public:
    bool isPalindrome(int x) {
        long a = 0;
        int l = x;
        if(x<0){
            return false;
        }
        while(x!=0){
            int LD = x%10;
            x = x/10;
            a = a*10+LD; 
        }
        return l == a;
        }

};