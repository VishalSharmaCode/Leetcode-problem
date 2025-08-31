class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1   # must split into at least 2 numbers

        dp = [0] * (n + 1)
        dp[1], dp[2], dp[3] = 1, 1, 2

        for i in range(4, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        
        return dp[n]