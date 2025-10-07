from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        next_rain = defaultdict(list)
        for i, lake in enumerate(rains):
            if lake > 0:
                next_rain[lake].append(i)
        
        full = set()
        heap = []
        ans = []
        
        for i, lake in enumerate(rains):
            if lake > 0:  # raining
                if lake in full:  # flood
                    return []
                full.add(lake)
                next_rain[lake].pop(0)
                if next_rain[lake]:
                    heappush(heap, (next_rain[lake][0], lake))
                ans.append(-1)
            else:  # dry day
                if heap:
                    _, dry_lake = heappop(heap)
                    full.remove(dry_lake)
                    ans.append(dry_lake)
                else:
                    ans.append(1)  # arbitrary
        return ans
