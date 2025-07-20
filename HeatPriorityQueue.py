# ------------------------------
# Heapsort Implementation
# ------------------------------

def heapify(arr, n, i):
    """
    Maintains max-heap property for subtree rooted at index i.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapsort(arr):
    """
    Sorts an array in ascending order using Heapsort.
    """
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # swap
        heapify(arr, i, 0)

    return arr


# ------------------------------
# Task Class for Priority Queue
# ------------------------------

class Task:
    def __init__(self, task_id, priority, arrival_time=None, deadline=None):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        # For min-heap, lower priority value means higher priority
        return self.priority < other.priority

    def __repr__(self):
        return f"Task(id={self.task_id}, priority={self.priority})"


# ------------------------------
# Priority Queue Implementation
# ------------------------------

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        """
        Inserts a new task into the priority queue.
        """
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        """
        Removes and returns the task with the highest priority.
        """
        if self.is_empty():
            return None
        max_task = self.heap[0]
        last_task = self.heap.pop()
        if self.heap:
            self.heap[0] = last_task
            self._heapify_down(0)
        return max_task

    def increase_key(self, index, new_priority):
        """
        Increases the priority of the task at index.
        """
        if index < 0 or index >= len(self.heap):
            return
        if new_priority < self.heap[index].priority:
            raise ValueError("New priority is lower than current priority.")
        self.heap[index].priority = new_priority
        self._heapify_up(index)

    def is_empty(self):
        """
        Checks if the priority queue is empty.
        """
        return len(self.heap) == 0

    # Internal helper methods

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index].priority > self.heap[parent].priority:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        n = len(self.heap)
        largest = index

        left = 2 * index + 1
        right = 2 * index + 2

        if left < n and self.heap[left].priority > self.heap[largest].priority:
            largest = left
        if right < n and self.heap[right].priority > self.heap[largest].priority:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)


# ------------------------------
# Demonstration / Test Code
# ------------------------------

if __name__ == "__main__":
    print("=== Heapsort Demo ===")
    sample_array = [12, 11, 13, 5, 6, 7]
    print("Original array:", sample_array)
    sorted_array = heapsort(sample_array.copy())
    print("Sorted array:", sorted_array)

    print("\n=== Priority Queue Demo ===")
    pq = PriorityQueue()
    tasks = [Task('t1', 3), Task('t2', 5), Task('t3', 1), Task('t4', 4)]
    for task in tasks:
        print(f"Inserting {task}")
        pq.insert(task)

    print("\nExtracting tasks by priority:")
    while not pq.is_empty():
        task = pq.extract_max()
        print(f"Extracted: {task}")
