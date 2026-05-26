class Solution {
public:
    long long mySqrt(int x) {
        int st =0, end = x;
        long long ans=0;
        while(st<=end){
            long long mid = st+(end-st)/2;
            long long sqr = mid*mid;
            if(sqr==x){
                return mid;
            }
            else{
                if(sqr< x){
                    ans = mid;
                    st = mid+1;
                }
                else{
                    end = mid-1;
                }
            }
            
        }
        return ans;
    }
};