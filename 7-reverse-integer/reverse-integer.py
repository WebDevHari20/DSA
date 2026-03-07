class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 1. Sign ko pehle hi save kar lein
        sign = -1 if x < 0 else 1 
        
        # 2. x ko positive (absolute) bana dein taaki loop sahi chale
        x = abs(x)
        res = 0
        
        # 3. Mathematical reversal logic
        while x > 0:
            rem = x % 10          # Last digit nikala
            res = (res * 10) + rem  # Result mein shift karke add kiya
            x = x // 10           # Original number se last digit hataya
        
        # 4. Original sign wapas lagayein
        final_res = res * sign
        
        # 5. Overflow check (32-bit signed integer range)
        # Agar exact value yaad na rahe toh 2**31 use karein
        if final_res < -2**31 or final_res > 2**31 - 1:
            return 0
            
        return final_res