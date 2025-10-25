class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def numToList(num):
            li = []
            while num != 0:
                li.append(num%10)
                num = num//10
            return li[::-1]
        li3 = []
        for i in range(left,right+1):
            digits = numToList(i)
            if 0 in digits:
                continue
            if all(i%d ==0 for d in digits):
                li3.append(i)
        return li3



        