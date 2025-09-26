class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        
        for k in range(n - 1, 1, -1):  # fix largest side
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += (j - i)   # all nums[i..j-1] form valid pairs
                    j -= 1
                else:
                    i += 1
        return count