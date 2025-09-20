from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
from typing import List

class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = deque()   # FIFO: stores [source, destination, timestamp]
        self.seen = set()      # dedup check
        self.dest_map = defaultdict(list)  # destination -> sorted timestamps

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.seen:
            return False

        # evict oldest if over memory
        if len(self.queue) >= self.memoryLimit:
            old = self.queue.popleft()
            self.seen.remove(tuple(old))
            # remove timestamp from dest_map
            d = old[1]
            t = old[2]
            idx = bisect_left(self.dest_map[d], t)
            if idx < len(self.dest_map[d]) and self.dest_map[d][idx] == t:
                self.dest_map[d].pop(idx)

        # add new packet
        self.queue.append([source, destination, timestamp])
        self.seen.add(packet)

        # maintain sorted list (timestamps are non-decreasing)
        self.dest_map[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        packet = self.queue.popleft()
        self.seen.remove(tuple(packet))

        # remove from dest_map
        d, t = packet[1], packet[2]
        idx = bisect_left(self.dest_map[d], t)
        if idx < len(self.dest_map[d]) and self.dest_map[d][idx] == t:
            self.dest_map[d].pop(idx)

        return packet

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        arr = self.dest_map.get(destination, [])
        left = bisect_left(arr, startTime)
        right = bisect_right(arr, endTime)
        return right - left
