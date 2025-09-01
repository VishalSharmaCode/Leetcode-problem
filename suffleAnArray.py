import random
from typing import List

class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:]   # keep a copy of the original array
        self.array = nums[:]      # working array

    def reset(self) -> List[int]:
        self.array = self.original[:]   # restore original
        return self.array

    def shuffle(self) -> List[int]:
        shuffled = self.array[:]
        n = len(shuffled)
        for i in range(n - 1, 0, -1):   # Fisher-Yates algorithm
            j = random.randint(0, i)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        return shuffled


# Example usage:
# obj = Solution([1, 2, 3])
# print(obj.shuffle())  # random permutation
# print(obj.reset())    # [1, 2, 3]
# print(obj.shuffle())  # another random permutation