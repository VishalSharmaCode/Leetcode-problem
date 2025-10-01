class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles   # all initially full bottles will be drunk
        empty = numBottles   # all become empty after drinking
        
        while empty >= numExchange:
            new_bottles = empty // numExchange    # how many full bottles we get
            total += new_bottles                  # drink them
            empty = empty % numExchange + new_bottles  # remaining empty + new empty
        
        return total