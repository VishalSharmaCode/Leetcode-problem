from typing import List
import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        min_heap = []
        current_max = float('-inf')
        
        # Step 1: Insert first element of each list
        for i in range(k):
            val = nums[i][0]
            heapq.heappush(min_heap, (val, i, 0))  # (value, list_index, element_index)
            current_max = max(current_max, val)
        
        best_range = [float('-inf'), float('inf')]
        
        while True:
            current_min, list_idx, elem_idx = heapq.heappop(min_heap)
            
            # Update best range
            if current_max - current_min < best_range[1] - best_range[0] or \
            (current_max - current_min == best_range[1] - best_range[0] and current_min < best_range[0]):
                best_range = [current_min, current_max]
            
            # Move pointer in the same list
            if elem_idx + 1 == len(nums[list_idx]):
                break  # One list exhausted
            
            next_val = nums[list_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, elem_idx + 1))
            current_max = max(current_max, next_val)
        
        return best_range