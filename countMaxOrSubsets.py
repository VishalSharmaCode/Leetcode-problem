class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.max_or = 0
        self.count = 0

        def dfs(index, curr_or):
            if index == len(nums):
                if curr_or == self.max_or:
                    self.count += 1
                return

            # Include current number
            dfs(index + 1, curr_or | nums[index])

            # Exclude current number
            dfs(index + 1, curr_or)

        # First, find the max possible OR
        for num in nums:
            self.max_or |= num

        # Now, use DFS to count subsets with max OR
        dfs(0, 0)
        return self.count