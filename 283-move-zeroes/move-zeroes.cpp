class Solution {
public:
    void moveZeroes(vector<int>& arr) {
        int n = arr.size();
        int st = 0;
        for(int i = 0; i<n;i++){
            if(arr[i]!=0){
                swap(arr[st], arr[i]);
                st++;
            }
        }
    }
};