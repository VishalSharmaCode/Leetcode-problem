class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        # prefix sums of skills: S[i] = sum_{k=0..i} skill[k]
        S = [0] * n
        S[0] = skill[0]
        for i in range(1, n):
            S[i] = S[i-1] + skill[i]

        total = 0
        # handle case m == 1: sum_{i} skill[i] * mana[0]
        if m == 1:
            return S[-1] * mana[0]

        # for each j from 0 .. m-2 compute delta_j
        for j in range(m - 1):
            mj = mana[j]
            mj1 = mana[j + 1]
            best = -10**30
            # iterate i = 0..n-1. S_{i-1} is 0 when i==0
            prev_S = 0  # S_{i-1}
            for i in range(n):
                Si = S[i]
                val = mj * Si - mj1 * prev_S
                if val > best:
                    best = val
                prev_S = Si  # for next iteration prev_S = S[i]
            total += best

        # add finishing time of last potion (sum of skill * last mana)
        total += S[-1] * mana[-1]
        return total