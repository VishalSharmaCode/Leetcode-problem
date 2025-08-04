class Solution:
    def combine(self, n: int, k: int):
        result = []

        def backtrack(start, path):
            if len(path) == k:
                result.append(path[:])  # Add a copy of the current path
                return
            for i in range(start, n + 1):
                path.append(i)              # Choose
                backtrack(i + 1, path)      # Explore
                path.pop()                  # Un-choose (backtrack)

        backtrack(1, [])
        return result