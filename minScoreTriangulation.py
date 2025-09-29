class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        
        # gap = length of subpolygon
        for length in range(3, n+1):  # polygon must have at least 3 vertices
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float("inf")
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j],
                                   dp[i][k] + dp[k][j] + values[i] * values[j] * values[k])
        
        return dp[0][n-1]