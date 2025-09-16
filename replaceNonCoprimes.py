from math import gcd
from typing import List

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        
        for num in nums:
            stack.append(num)
            
            # keep merging top two while non-coprime
            while len(stack) > 1:
                a, b = stack[-2], stack[-1]
                g = gcd(a, b)
                if g == 1:  # coprime → stop merging
                    break
                # replace with LCM
                lcm = a * b // g
                stack.pop()
                stack[-1] = lcm   # update top with merged value
        
        return stack