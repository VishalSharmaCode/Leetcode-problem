from collections import Counter
import bisect
from typing import List

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        if not power:
            return 0

        cnt = Counter(power)
        values = sorted(cnt.keys())
        totals = [v * cnt[v] for v in values]
        n = len(values)

        dp = [0] * n
        dp[0] = totals[0]

        for i in range(1, n):
            # find largest index j < i with values[j] <= values[i] - 3
            # bisect_right returns first index > (values[i]-3), so subtract 1
            j = bisect.bisect_right(values, values[i] - 3) - 1
            take = totals[i] + (dp[j] if j >= 0 else 0)
            dp[i] = max(dp[i-1], take)

        return dp[-1]