class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        arr = []
        l, r = 0, len(matrix[0])
        t, b = 0, len(matrix)
        while l < r and t < b:
            for i in range(l,r):
                arr.append(matrix[t][i])
            t +=1
            for i in range(t, b):
                arr.append(matrix[i][r-1])
            r -= 1
            if not (l < r and t < b):
                break
            for i in range(r -1, l-1, -1):
                arr.append(matrix[b-1][i])
            b -= 1
            for i in range(b-1, t-1, -1):
                arr.append(matrix[i][l])
            l += 1
        return arr