class Solution:
    def smallestSubarrays(self, nums):
        n = len(nums)
        answer = [0] * n
        last = [0] * 32  # Last seen position for each bit

        for i in range(n - 1, -1, -1):
            for b in range(32):
                if nums[i] & (1 << b):
                    last[b] = i  # Update last position where bit b is seen

            max_len = 1
            for pos in last:
                if pos > i:
                    max_len = max(max_len, pos - i + 1)

            answer[i] = max_len

        return answer