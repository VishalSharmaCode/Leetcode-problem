from typing import List 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the value and its index
        num_to_index = {}
        
        # Iterate through the list of numbers
        for index, num in enumerate(nums):
            # Calculate the complement of the current number
            complement = target - num
            
            # Check if the complement is already in the dictionary
            if complement in num_to_index:
                # If it is, return the indices of the complement and the current number
                return [num_to_index[complement], index]
            
            # Otherwise, add the current number and its index to the dictionary
            num_to_index[num] = index
        
        # Return an empty list if no solution is found
        # (According to the problem statement, this should never be reached)
        return []
x = Solution()
print(x.twoSum([2, 7, 11, 15], 9))