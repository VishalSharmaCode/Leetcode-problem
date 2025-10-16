class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        from collections import Counter
        
        # Normalize each number modulo value
        count = Counter(((num % value) + value) % value for num in nums)
        # Try to form numbers starting from 0 upwards
        mex = 0
        while count[mex % value] > 0:
            count[mex % value] -= 1
            mex += 1
        return mex