class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []
        
        # Step 1: Push all boundary cells into min-heap
        for i in range(m):
            for j in range(n):
                if i in (0, m-1) or j in (0, n-1):
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        water = 0
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # Step 2: Process heap
        while heap:
            height, x, y = heapq.heappop(heap)
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    nh = heightMap[nx][ny]
                    # If neighbor lower, trap water
                    if nh < height:
                        water += height - nh
                    # Push new boundary (max ensures water can't flow out)
                    heapq.heappush(heap, (max(height, nh), nx, ny))
        
        return water