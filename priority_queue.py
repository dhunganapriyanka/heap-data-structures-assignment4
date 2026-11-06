
from dataclasses import dataclass


@dataclass
class Task:
    task_id: int
    priority: int
    arrival_time: int
    deadline: int


class PriorityQueue:
    """Max-heap priority queue using a Python list."""

    def __init__(self):
        self.heap = []
        self.positions = {}

    def _higher(self, a, b):
        # Larger priority comes first.
        # Earlier arrival breaks ties.
        if a.priority != b.priority:
            return a.priority > b.priority
        return (a.arrival_time, a.task_id) < (
            b.arrival_time, b.task_id
        )

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = (
            self.heap[j], self.heap[i]
        )
        self.positions[self.heap[i].task_id] = i
        self.positions[self.heap[j].task_id] = j

    def _sift_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if not self._higher(
                self.heap[index], self.heap[parent]
            ):
                break
            self._swap(index, parent)
            index = parent

    def _sift_down(self, index):
        n = len(self.heap)
        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < n and self._higher(
                self.heap[left], self.heap[largest]
            ):
                largest = left

            if right < n and self._higher(
                self.heap[right], self.heap[largest]
            ):
                largest = right

            if largest == index:
                break

            self._swap(index, largest)
            index = largest

    def insert(self, task):
        if task.task_id in self.positions:
            raise ValueError("Duplicate task ID")

        self.heap.append(task)
        index = len(self.heap) - 1
        self.positions[task.task_id] = index
        self._sift_up(index)

    def extract_max(self):
        if self.is_empty():
            return None

        highest = self.heap[0]
        last = self.heap.pop()
        del self.positions[highest.task_id]

        if self.heap:
            self.heap[0] = last
            self.positions[last.task_id] = 0
            self._sift_down(0)

        return highest

    def change_priority(self, task_id, new_priority):
        if task_id not in self.positions:
            raise KeyError("Task not found")

        index = self.positions[task_id]
        old_priority = self.heap[index].priority
        self.heap[index].priority = new_priority

        if new_priority > old_priority:
            self._sift_up(index)
        elif new_priority < old_priority:
            self._sift_down(index)

    def increase_key(self, task_id, new_priority):
        index = self.positions[task_id]
        if new_priority < self.heap[index].priority:
            raise ValueError("Priority must increase")
        self.change_priority(task_id, new_priority)

    def decrease_key(self, task_id, new_priority):
        index = self.positions[task_id]
        if new_priority > self.heap[index].priority:
            raise ValueError("Priority must decrease")
        self.change_priority(task_id, new_priority)

    def is_empty(self):
        return len(self.heap) == 0


if __name__ == "__main__":
    pq = PriorityQueue()

    pq.insert(Task(1, 3, 0, 10))
    pq.insert(Task(2, 5, 1, 8))
    pq.insert(Task(3, 2, 2, 12))
    pq.insert(Task(4, 4, 3, 9))

    print("Priority Queue Test")
    print("----------------------")
    print("Queue empty?", pq.is_empty())

    pq.increase_key(3, 6)
    print("Task 3 priority increased to 6")

    pq.decrease_key(2, 1)
    print("Task 2 priority decreased to 1")

    print("\nProcessing tasks:")
    while not pq.is_empty():
        task = pq.extract_max()
        print(
            f"Task {task.task_id}, "
            f"Priority {task.priority}, "
            f"Deadline {task.deadline}"
        )

    print("\nQueue empty?", pq.is_empty())
