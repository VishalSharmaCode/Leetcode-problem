from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)

        for i in range(1, n - 1):
            # Skip duplicates
            if nums[i] == nums[i - 1]:
                continue
            
            # Find left neighbor that's not equal
            left = i - 1
            while left >= 0 and nums[left] == nums[i]:
                left -= 1
            
            # Find right neighbor that's not equal
            right = i + 1
            while right < n and nums[right] == nums[i]:
                right += 1
            
            if left >= 0 and right < n:
                if nums[i] > nums[left] and nums[i] > nums[right]:
                    count += 1  # Hill
                elif nums[i] < nums[left] and nums[i] < nums[right]:
                    count += 1  # Valley
        
        return count