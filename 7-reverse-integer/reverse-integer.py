class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1 
        x = abs(x)
        res = 0
        while x > 0:
            rem = x % 10          
            res = (res * 10) + rem  
            x = x // 10           
    
        final_res = res * sign
        
        if final_res < -2**31 or final_res > 2**31 - 1:
            return 0
            
        return final_res