class Solution:
    def nextPermutation(nums):
        n = len(nums)
        pivot = -1
        
        # Step 1: Find the first decreasing element from the right
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break
        
        # If no pivot is found, the array is in descending order (last permutation)
        if pivot == -1:
            nums.reverse()
            return

        # Step 2: Find the number to swap with the pivot
        for i in range(n - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break
        
        # Step 3: Reverse the elements to the right of the pivot
        left, right = pivot + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1