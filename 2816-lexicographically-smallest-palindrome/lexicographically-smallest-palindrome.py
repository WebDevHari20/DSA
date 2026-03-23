class Solution(object):
    def makeSmallestPalindrome(self, s):
        s = list(s)
        i, j = 0, len(s)-1
        while i<j:
            if s[i] != s[j]:
                smallest = min(s[i], s[j])
                s[i] = smallest
                s[j] = smallest
            i += 1
            j-=1
        return "".join(s)