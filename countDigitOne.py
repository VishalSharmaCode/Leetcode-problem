class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        pos = 1  # position: 1 (ones), 10 (tens), 100 (hundreds), ...

        while pos <= n:
            high = n // (pos * 10)
            curr = (n // pos) % 10
            low = n % pos

            if curr == 0:
                count += high * pos
            elif curr == 1:
                count += high * pos + low + 1
            else:
                count += (high + 1) * pos

            pos *= 10

        return count