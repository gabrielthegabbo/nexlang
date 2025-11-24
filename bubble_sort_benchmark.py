import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Generate list of 100 numbers in reverse order
test_list = list(range(100, 0, -1))

print("Python Bubble Sort Benchmark")
print("Sorting 100 elements...")

start_time = time.time()
sorted_list = bubble_sort(test_list.copy())
end_time = time.time()

elapsed_time = (end_time - start_time) * 1000  # Convert to milliseconds

print(f"Time elapsed: {elapsed_time:.2f} ms")
print(f"First 10 elements: {sorted_list[:10]}")
print(f"Last 10 elements: {sorted_list[-10:]}")
