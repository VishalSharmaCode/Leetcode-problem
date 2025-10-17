from functools import lru_cache

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        a = [ord(c) - 97 for c in s]  # convert chars to numbers 0–25

        @lru_cache(None)
        def dfs(i, mask, changed):
            if i == n:
                return 0
            res = 0
            cur_mask = mask | (1 << a[i])

            # if current set of distinct chars exceeds k, start new partition
            if bin(cur_mask).count("1") > k:
                res = 1 + dfs(i + 1, 1 << a[i], changed)
            else:
                res = dfs(i + 1, cur_mask, changed)

            # try changing this char (only once)
            if not changed:
                for c in range(26):
                    if c == a[i]:
                        continue
                    new_mask = mask | (1 << c)
                    if bin(new_mask).count("1") > k:
                        res = max(res, 1 + dfs(i + 1, 1 << c, True))
                    else:
                        res = max(res, dfs(i + 1, new_mask, True))
            return res

        return dfs(0, 0, False) + 1
