
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def twoSum(nums, target):
    index_map = {}  # Stores number -> index
    for i, num in enumerate(nums):
        diff = target - num
        if diff in index_map:
            return [index_map[diff], i]
        index_map[num] = i
    return []

# Example usage:
arr = [2, 5, 5, 11]
x = twoSum(arr, 10)
print(x)