class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        inc = [1] * n

        # Step 1: Compute length of increasing subarray ending at each index
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc[i] = inc[i - 1] + 1

        # Step 2: Compute length of increasing subarray starting at each index
        dec = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                dec[i] = dec[i + 1] + 1

        # Step 3: Find maximum k where two adjacent increasing subarrays exist
        ans = 0
        for i in range(1, n):
            ans = max(ans, min(inc[i - 1], dec[i]))

        return ans