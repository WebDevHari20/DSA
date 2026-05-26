class Solution {
public:
    int search(vector<int>& arr, int k) {
        int st = 0 , end = arr.size()-1;
        while(st<=end){
            int mid = st + (end - st)/2;
            if(arr[mid]==k) return mid;
            if(arr[mid]>=arr[st]){
               if(arr[mid]>k&&arr[st]<=k){
                end=mid-1;
               }
               else{
                st=mid+1;
               }
            }
            else{
                if(arr[mid]<k && arr[end]>=k){
                    st = mid+1;
                }else{
                    end=mid-1;
                }
            }
        }
        return -1;
    }
};