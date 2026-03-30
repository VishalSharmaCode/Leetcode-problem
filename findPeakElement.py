from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maxNum = nums[0]
        for i in range(len(nums)):
            maxNum = max(maxNum, nums[i])
        for i in range(len(nums)):
            if nums[i]== maxNum:
                return i
        