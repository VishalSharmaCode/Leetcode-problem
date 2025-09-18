
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_info = {}   # taskId -> (userId, priority)
        self.heap = []        # max-heap as (-priority, -taskId, userId)
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_info[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _ = self.task_info[taskId]
        self.task_info[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, userId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_info:
            del self.task_info[taskId]

    def execTop(self) -> int:
        while self.heap:
            negP, negT, _ = heapq.heappop(self.heap)
            taskId = -negT
            priority = -negP

            info = self.task_info.get(taskId)
            if info is None:
                # task was removed or re-added under a different id; skip
                continue

            cur_user, cur_pr = info
            if cur_pr != priority:
                # outdated priority entry, skip
                continue

            # valid — remove from mapping and return the current userId (authoritative)
            del self.task_info[taskId]
            return cur_user
        return -1