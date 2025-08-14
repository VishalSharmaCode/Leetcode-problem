class SolutionOne:
    def countPrimes(self, n: int) -> int:
        def prime(num):
            count = 0
            for i in range(2,num//2+1):
                if num%i==0:
                    count += 1
            if(count == 0):
                return True
            else:
                return False
        arr = []
        for i in range(2, n):
            if(prime(i)==True):
                arr.append(i)
        return len(arr)

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        # Step 1: Create a boolean array
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
        
        # Step 2: Sieve
        p = 2
        while p * p < n:
            if is_prime[p]:
                # Mark multiples of p as False
                for multiple in range(p * p, n, p):
                    is_prime[multiple] = False
            p += 1
        
        # Step 3: Count primes
        return sum(is_prime)