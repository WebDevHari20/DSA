#include <vector>
#include <numeric> // For std::gcd

using namespace std;

class Solution {
public:
    long long getLCM(long long a, long long b) {
        if (a == 0 || b == 0) return 0;
        return (a * b) / gcd(a, b);
    }

    int subarrayLCM(vector<int>& nums, int k) {
        int count = 0;
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            long long currentLCM = nums[i];

            for (int j = i; j < n; j++) {

                currentLCM = getLCM(currentLCM, (long long)nums[j]);

                if (currentLCM > k) break;

                
                if (currentLCM == k) {
                    count++;
                }


            }
        }

        return count;
    }
};