import sys
from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        
        baskets_temp = list(baskets)
        
        tree = [0] * (4 * n)
        
        sys.setrecursionlimit(max(sys.getrecursionlimit(), 2 * n + 50))

        def build(node: int, start: int, end: int):
            if start == end:
                tree[node] = baskets_temp[start]
            else:
                mid = (start + end) // 2
                build(2 * node, start, mid)
                build(2 * node + 1, mid + 1, end)
                tree[node] = max(tree[2 * node], tree[2 * node + 1])

        def update(node: int, start: int, end: int, idx: int, val: int):
            if start == end:
                tree[node] = val
            else:
                mid = (start + end) // 2
                if start <= idx <= mid:
                    update(2 * node, start, mid, idx, val)
                else:
                    update(2 * node + 1, mid + 1, end, idx, val)
                tree[node] = max(tree[2 * node], tree[2 * node + 1])

        def find_leftmost(node: int, start: int, end: int, required_capacity: int) -> int | None:
            if tree[node] < required_capacity:
                return None

            if start == end:
                return start

            mid = (start + end) // 2
            
            result = find_leftmost(2 * node, start, mid, required_capacity)
            if result is not None:
                return result
            
            return find_leftmost(2 * node + 1, mid + 1, end, required_capacity)

        if n > 0:
            build(1, 0, n - 1)

        unplaced_count = 0
        for fruit_cap in fruits:
            basket_idx = find_leftmost(1, 0, n - 1, fruit_cap)
            
            if basket_idx is not None:
                update(1, 0, n - 1, basket_idx, 0)
            else:
                unplaced_count += 1
                
        return unplaced_count