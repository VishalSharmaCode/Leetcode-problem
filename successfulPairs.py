import bisect

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        res = []
        
        for spell in spells:
            # Minimum required potion strength
            min_potion = (success + spell - 1) // spell  # ceil(success / spell)
            
            # Binary search for first potion >= min_potion
            idx = bisect.bisect_left(potions, min_potion)
            
            # Count of successful potions
            res.append(m - idx)
        
        return res