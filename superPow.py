class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        mod = 1337
        def mod_pow(x,n):
            res = 1
            x %= mod
            while n > 0:
                if n%2:
                    res = (res*x)%mod
                x = (x*x)%mod
                n //=2
            return res
        if not b:
            return 1
        last_digit = b.pop()
        p1 = mod_pow(a,last_digit)
        p2 = mod_pow(self.superPow(a,b),10)
        return (p1*p2)%mod        