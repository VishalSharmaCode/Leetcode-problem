class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count1 = Counter(basket1)
        count2 = Counter(basket2)
        total = count1 + count2

        # Step 1: Check if total frequency is even for all fruits
        for k in total:
            if total[k] % 2 != 0:
                return -1

        # Step 2: Find surplus in both baskets
        surplus1 = []
        surplus2 = []
        for fruit in total:
            diff = count1[fruit] - count2[fruit]
            if diff > 0:
                surplus1.extend([fruit] * (diff // 2))
            elif diff < 0:
                surplus2.extend([fruit] * (-diff // 2))

        # Step 3: Sort to match lowest with highest to minimize cost
        surplus1.sort()
        surplus2.sort(reverse=True)

        min_elem = min(min(basket1), min(basket2))
        cost = 0
        for a, b in zip(surplus1, surplus2):
            cost += min(min(a, b), 2 * min_elem)

        return cost