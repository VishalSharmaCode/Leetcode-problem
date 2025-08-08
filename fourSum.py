class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, quad = [], []

        def kSum(k, start, target):
            if k == 2:
                l, r = start, len(nums) - 1
                while l < r:
                    curr_sum = nums[l] + nums[r]
                    if curr_sum < target:
                        l += 1
                    elif curr_sum > target:
                        r -= 1
                    else:
                        res.append(quad + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        # Skip duplicates
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                return

            for i in range(start, len(nums) - k + 1):
                # Pruning: Skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue
                # Early termination: if smallest or largest k nums can't reach target
                if nums[i] * k > target:
                    break
                if nums[-1] * k < target:
                    break
                quad.append(nums[i])
                kSum(k - 1, i + 1, target - nums[i])
                quad.pop()

        kSum(4, 0, target)
        return res