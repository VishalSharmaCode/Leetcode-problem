class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def arrCreation(n):
            return [i for i in range(1, n + 1)]

        def find_permutations_iterative():
            numbers = arrCreation(n)
            permutations = [list(numbers)]
            length = len(numbers)

            while True:
                m = -1
                for i in range(length - 2, -1, -1):  # fixed index range
                    if numbers[i] < numbers[i + 1]:
                        m = i
                        break
                if m == -1:
                    break

                l = -1
                for i in range(length - 1, m, -1):
                    if numbers[m] < numbers[i]:
                        l = i
                        break

                numbers[m], numbers[l] = numbers[l], numbers[m]
                numbers[m + 1:] = reversed(numbers[m + 1:])
                permutations.append(list(numbers))

            return permutations

        def combine(arr):
            x = arr[0]
            for i in range(1, len(arr)):
                x = x * 10 + arr[i]
            return str(x)

        res = find_permutations_iterative()[k - 1]  # fixed indexing
        return combine(res)


class SolutionSecond:
    def getPermutation(self, n: int, k: int) -> str:
        def arrCreation(n):
            arr = []
            for i in range(1, n+1):
                arr.append(i)
            return arr

        def find_kth_permutation(n, k):
            from math import factorial
            numbers = arrCreation(n)
            k -= 1  # convert to 0-index
            result = []
            
            for i in range(n, 0, -1):
                fact = factorial(i - 1)
                index = k // fact
                result.append(numbers.pop(index))
                k %= fact
            
            return result

        def combine(arr):
            x = arr[0]
            for i in range(1, len(arr)):
                x = x * 10
                x = x + arr[i]
            return str(x)

        res = find_kth_permutation(n, k)
        return combine(res)