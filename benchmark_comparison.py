import time
from run import run

def benchmark_comparison():
    # Python benchmark
    print("=" * 60)
    print("BUBBLE SORT PERFORMANCE COMPARISON")
    print("=" * 60)
    
    # Python implementation
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
    
    python_list = list(range(100, 0, -1))
    
    print("\n[1] Python Native Implementation")
    print("-" * 60)
    start = time.time()
    result = bubble_sort(python_list.copy())
    python_time = (time.time() - start) * 1000
    print(f"Time: {python_time:.2f} ms")
    print(f"Sorted: {result[:5]}...{result[-5:]}")
    
    # Nex language benchmark
    print("\n[2] Nex Language Implementation")
    print("-" * 60)
    
    with open("nexoraq.nex", "r") as f:
        script = f.read()
    
    start = time.time()
    _, error = run("nexoraq.nex", script)
    nex_time = (time.time() - start) * 1000
    
    if error:
        print(f"Error: {error.as_string()}")
    else:
        print(f"Time: {nex_time:.2f} ms")
    
    # Comparison
    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    print(f"Python:    {python_time:.2f} ms")
    print(f"Nex:       {nex_time:.2f} ms")
    print(f"Slowdown:  {nex_time/python_time:.1f}x slower")
    print("=" * 60)

if __name__ == "__main__":
    benchmark_comparison()
