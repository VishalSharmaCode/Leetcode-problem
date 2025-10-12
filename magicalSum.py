class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        MAX_CARRY = 30  # Max carry is around 29 or 30 for m <= 30

        # 1. Pre-calculate factorials and inverse factorials
        fact = [1] * (m + 1)
        inv_fact = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = (fact[i - 1] * i) % MOD

        # Modular inverse function using Fermat's Little Theorem
        def power(a, b):
            res = 1
            a %= MOD
            while b > 0:
                if b % 2 == 1:
                    res = (res * a) % MOD
                a = (a * a) % MOD
                b //= 2
            return res

        inv_fact[m] = power(fact[m], MOD - 2)
        for i in range(m - 1, -1, -1):
            inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

        # 2. Pre-calculate terms nums[i]^c / c!
        term_coeffs = [[0] * (m + 1) for _ in range(n)]
        for i in range(n):
            current_pow = 1
            for c in range(m + 1):
                term_coeffs[i][c] = (current_pow * inv_fact[c]) % MOD
                current_pow = (current_pow * nums[i]) % MOD

        # Function to count set bits
        def popcount(x):
            count = 0
            while x > 0:
                count += x & 1
                x >>= 1
            return count

        # 3. Dynamic Programming
        # dp[i][count][carry][set_bits]
        # i: index of nums considered (0 to n)
        # count: total number of elements chosen so far (0 to m)
        # carry: carry into the i-th bit (0 to MAX_CARRY)
        # set_bits: total set bits in the number formed by bits 0 to i-1 (0 to k)
        
        # Initialize DP table: (i, count, carry, set_bits)
        # The number of states for i is n+1, but we only use two levels at a time (current and next)
        # for space optimization, but for clarity, we use the full table.
        # Python list size: (n + 1) x (m + 1) x (MAX_CARRY + 1) x (k + 1)
        
        dp = [[[[0] * (k + 1) for _ in range(MAX_CARRY + 1)] for _ in range(m + 1)] for _ in range(n + 1)]

        # Base Case: dp[0][0][0][0] = 1
        dp[0][0][0][0] = 1

        for i in range(n):
            for count in range(m + 1):
                for carry in range(MAX_CARRY + 1):
                    for set_bits in range(k + 1):
                        if dp[i][count][carry][set_bits] == 0:
                            continue

                        # Iterate over c_i: number of times index i is chosen
                        for c_i in range(m - count + 1):
                            current_sum = c_i + carry
                            b_i = current_sum % 2  # i-th bit of S
                            next_carry = current_sum // 2
                            next_count = count + c_i
                            next_set_bits = set_bits + b_i

                            if next_carry <= MAX_CARRY and next_set_bits <= k:
                                factor = term_coeffs[i][c_i]
                                
                                term = (dp[i][count][carry][set_bits] * factor) % MOD
                                dp[i + 1][next_count][next_carry][next_set_bits] = \
                                    (dp[i + 1][next_count][next_carry][next_set_bits] + term) % MOD

        # 4. Final Calculation
        # Sum over all valid final states dp[n][m][carry][set_bits]
        # The total set bits must be k: set_bits + popcount(carry) = k
        
        total_sum_product = 0
        for carry in range(MAX_CARRY + 1):
            carry_set_bits = popcount(carry)
            
            # Check if remaining set bits are non-negative and within k
            required_set_bits = k - carry_set_bits
            if 0 <= required_set_bits <= k:
                # dp[n][m][carry][required_set_bits]
                total_sum_product = (total_sum_product + dp[n][m][carry][required_set_bits]) % MOD

        # Multiply by m!
        final_result = (total_sum_product * fact[m]) % MOD
        
        return final_result