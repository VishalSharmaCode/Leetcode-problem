class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for i in range(len(nums)):
            if nums[i] == target:
                arr.append(i)
        if arr:
            if len(arr)<=1:
                arr.append(arr[0])
            return [arr[0], arr[len(arr)-1]]
        else:
            return [-1,-1]