class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        nums1_copy = nums1.copy()
        nums2_copy = nums2.copy()

        if len(nums1_copy) <= len(nums2_copy):
            for num in nums1:
                if num in nums2_copy:
                    arr.append(num)
                    nums2_copy.remove(num)
        else:
            for num in nums2:
                if num in nums1_copy:
                    arr.append(num)
                    nums1_copy.remove(num)
        return arr

# Optimized solution using Counter
 
from collections import Counter

class OptimizedSolution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        arr = []

        for num in nums2:
            if count1[num] > 0:
                arr.append(num)
                count1[num] -= 1
        return arr