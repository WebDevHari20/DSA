class Solution(object):
    def __init__(self):
        self.memo = {}

    def isScramble(self, s1, s2):
        # Base cases
        if s1 == s2:
            return True
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            return False
        
        # Check memoization
        state = (s1, s2)
        if state in self.memo:
            return self.memo[state]
        
        n = len(s1)
        for i in range(1, n):
            # Case 1: No Swap
            # Compare s1's prefix with s2's prefix, and s1's suffix with s2's suffix
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                self.memo[state] = True
                return True
            
            # Case 2: Swap
            # Compare s1's prefix with s2's suffix, and s1's suffix with s2's prefix
            if self.isScramble(s1[:i], s2[n-i:]) and self.isScramble(s1[i:], s2[:n-i]):
                self.memo[state] = True
                return True
        
        self.memo[state] = False
        return False