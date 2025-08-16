class Solution:
    def addDigits(self, num: int) -> int:
        def merger(n):
            s = 0
            while n != 0:
                s = s+(n%10)
                n //=10
            if s >= 10:
                s = merger(s)
            return s
        return merger(num)