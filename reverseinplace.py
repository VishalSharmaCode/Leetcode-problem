from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        # First Solution

        # left = 0
        # right = len(s) - 1
        
        # while left < right:
        #     s[left], s[right] = s[right], s[left]
        #     left += 1
        #     right -= 1

        # Pythonic Solution
        s.reverse()