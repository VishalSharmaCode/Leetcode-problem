class Solution:
    def firstBadVersion(n):
        low = 1
        high = n
        
        while low < high:
            # Standard way to find the middle
            mid = low + (high - low) // 2
            
            if isBadVersion(mid):
                # If mid is bad, the first bad version is mid or earlier
                high = mid
            else:
                # If mid is good, the first bad version is definitely after mid
                low = mid + 1
        
        # When low == high, we've found the first bad version
        return low