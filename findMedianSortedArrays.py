from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        if len(nums1)%2 !=0:
            return float(nums1[len(nums1)//2])
        else:
            mid = len(nums1)//2
            pre_mid = mid-1
            res = (nums1[mid]+nums1[pre_mid])/2
            return res