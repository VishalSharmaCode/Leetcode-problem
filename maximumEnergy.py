class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = energy[:]  # copy
        
        # Traverse backwards to fill dp
        for i in range(n - k - 1, -1, -1):
            dp[i] += dp[i + k]
        
        return max(dp)