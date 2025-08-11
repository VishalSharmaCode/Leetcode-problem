class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # Step 1: Transpose
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()
    def my_solution(self, a: List[List[int]]):
        a = [[1,2,3],[4,5,6],[7,8,9]]
        arr = []

        for j in range(len(a)):
            arr1 = []
            for i in a:
                arr1.append(i[j])
            arr1 = arr1[::-1]
            arr.append(arr1)
        return arr
