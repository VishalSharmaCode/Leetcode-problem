class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr = [[1]]
        for i in range(rowIndex):
            temp = [0]+arr[-1]+[0]
            arr1 = []
            for j in range(len(arr[-1])+1):
                arr1.append(temp[j]+temp[j+1])
            arr.append(arr1)
        return arr[rowIndex]