class Solution:
    def maxSubArray(nums):
         maxsub = nums[0]
         count = 0
         for i in nums:
            if count < 0:
                count = 0
            count += i
            maxsub = max(maxsub,count)
         return maxsub