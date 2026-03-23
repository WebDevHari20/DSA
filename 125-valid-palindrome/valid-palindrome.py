class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = ""
        for ch in s:
            if ch.isalnum():
                result += ch.lower()
        return result == result[::-1]
