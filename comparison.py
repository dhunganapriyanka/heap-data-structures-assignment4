
import random
import time
from heapsort import heapsort


# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Randomized Quicksort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# Measure execution time
def measure_time(algorithm, data):
    start = time.perf_counter()
    result = algorithm(data.copy())
    elapsed = time.perf_counter() - start

    assert result == sorted(data)
    return elapsed


# Dataset sizes
sizes = [1000, 5000, 10000]

algorithms = {
    "Heapsort": heapsort,
    "Quicksort": quick_sort,
    "Merge Sort": merge_sort
}

for size in sizes:
    datasets = {
        "Sorted": list(range(size)),
        "Reverse": list(range(size, 0, -1)),
        "Random": random.sample(range(size * 10), size)
    }

    print(f"\nDataset Size: {size}")
    print("-" * 60)

    for data_type, data in datasets.items():
        print(f"\n{data_type} Data:")

        for name, algorithm in algorithms.items():
            times = [
                measure_time(algorithm, data)
                for _ in range(5)
            ]

            average_time = sum(times) / len(times)
            print(f"{name}: {average_time:.6f} seconds")
