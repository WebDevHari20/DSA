class Solution {
public:
    bool checkPerfectNumber(int num) {
        // 1 is not a perfect number, and negatives aren't either
        if (num <= 1) return false;

        int sum = 1; // Start with 1, as it's always a divisor
        
        // Loop from 2 up to the square root
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                sum += i;
                if (i * i != num) {
                    sum += num / i;
                }
            }
        }
        
        return sum == num;
    }
};