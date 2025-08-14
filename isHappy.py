class Solution:
    def isHappy(self, n: int) -> bool:
        def digitCount(num):
            count = 0
            while num != 0:
                count += (num % 10) ** 2
                num //= 10
            return count

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = digitCount(n)
        return n == 1