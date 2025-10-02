class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drunk = numBottles
        empty = numBottles

        while empty >= numExchange:
            # exchange once
            empty -= numExchange
            drunk += 1
            empty += 1  # new empty after drinking
            numExchange += 1  # exchange rate increases

        return drunk