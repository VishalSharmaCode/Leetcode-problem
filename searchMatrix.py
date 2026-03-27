class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        def binary(arr, tar):
            l, r = 0, len(arr)-1
            mid = (l+r)//2
            while l <= r:
                mid = (l+r)//2
                if arr[mid] > tar:
                    r = mid -1
                elif arr[mid] < tar:
                    l = mid + 1
                elif arr[mid] == tar:
                    return True
                else:
                    return False
        # for i in matrix:
        #     if target in i:
        #         return True
        # return False

        for i in matrix:
            if binary(i, target) == True:
                return True
        return False

