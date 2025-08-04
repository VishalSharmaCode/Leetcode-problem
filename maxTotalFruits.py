from bisect import bisect_left, bisect_right

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        prefix = [0] * (n + 1)

        # Build prefix sum of fruit amounts
        for i in range(n):
            prefix[i+1] = prefix[i] + fruits[i][1]

        res = 0

        # Try all possible left distances
        for x in range(k + 1):
            # Go left x steps, then right (k - 2*x) steps
            left = startPos - x
            right = startPos + max(0, k - 2 * x)

            l = bisect_left(fruits, [left])
            r = bisect_right(fruits, [right, float('inf')])
            res = max(res, prefix[r] - prefix[l])

            # Go right x steps, then left (k - 2*x) steps
            left = startPos - max(0, k - 2 * x)
            right = startPos + x

            l = bisect_left(fruits, [left])
            r = bisect_right(fruits, [right, float('inf')])
            res = max(res, prefix[r] - prefix[l])

        return res