class Solution(object):
    def isMatch(self, s, p):
        rows, cols = len(s), len(p)
        dp = [[False] * (cols + 1) for _ in range(rows + 1)]
        dp[0][0] = True

        for j in range(2, cols + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                else:
                    dp[i][j] = False

        return dp[rows][cols]