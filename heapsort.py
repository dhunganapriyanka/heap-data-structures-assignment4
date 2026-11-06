
def heapify(arr, heap_size, root):
    """Restore the max-heap property starting at root."""
    while True:
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2

        if left < heap_size and arr[left] > arr[largest]:
            largest = left

        if right < heap_size and arr[right] > arr[largest]:
            largest = right

        if largest == root:
            break

        arr[root], arr[largest] = arr[largest], arr[root]
        root = largest


def heapsort(arr):
    """Sort an array in ascending order using Heapsort."""
    n = len(arr)

    # Build a max-heap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Move the largest element to the sorted portion.
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


if __name__ == "__main__":
    test_cases = [
        [12, 11, 13, 5, 6, 7],
        [],
        [5],
        [4, 4, 2, 8, 2],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1]
    ]

    for case in test_cases:
        original = case.copy()
        result = heapsort(case)
        print(f"Original: {original}")
        print(f"Sorted:   {result}")
        print("-" * 30)
