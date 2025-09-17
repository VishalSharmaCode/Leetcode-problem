import heapq
from typing import List

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_to_heap = {}

        for f, c, r in zip(foods, cuisines, ratings):
            self.food_to_cuisine[f] = c
            self.food_to_rating[f] = r
            if c not in self.cuisine_to_heap:
                self.cuisine_to_heap[c] = []
            heapq.heappush(self.cuisine_to_heap[c], (-r, f))  # max-heap by rating, tie by lexicographic food

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_to_rating[food] = newRating
        cuisine = self.food_to_cuisine[food]
        heapq.heappush(self.cuisine_to_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_to_heap[cuisine]
        # Lazy deletion: discard outdated entries
        while heap:
            rating, food = heap[0]
            if -rating == self.food_to_rating[food]:
                return food
            heapq.heappop(heap)