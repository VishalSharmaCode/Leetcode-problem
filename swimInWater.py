import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False]*n for _ in range(n)]
        heap = [(grid[0][0], 0, 0)]  # (time, row, col)
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while heap:
            t, r, c = heapq.heappop(heap)
            if r == n - 1 and c == n - 1:
                return t  # Reached destination
            
            if visited[r][c]:
                continue
            visited[r][c] = True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))
