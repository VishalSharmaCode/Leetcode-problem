from sortedcontainers import SortedList

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        # Map (shop, movie) -> price
        self.price = {}
        for shop, movie, p in entries:
            self.price[(shop, movie)] = p

        # Available movies per movieId
        self.available = {}
        for shop, movie, p in entries:
            if movie not in self.available:
                self.available[movie] = SortedList()
            self.available[movie].add((p, shop))

        # Rented movies across all shops
        self.rented = SortedList()

    def search(self, movie: int) -> List[int]:
        if movie not in self.available:
            return []
        return [shop for _, shop in self.available[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        p = self.price[(shop, movie)]
        self.available[movie].remove((p, shop))
        self.rented.add((p, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        p = self.price[(shop, movie)]
        self.rented.remove((p, shop, movie))
        self.available[movie].add((p, shop))

    def report(self) -> List[List[int]]:
        return [[shop, movie] for p, shop, movie in self.rented[:5]]