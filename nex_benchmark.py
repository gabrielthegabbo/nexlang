import time
from run import run

print("=" * 50)
print("Nex Language Bubble Sort Benchmark")
print("=" * 50)

with open("nexoraq.nex", "r") as f:
    script = f.read()

start_time = time.time()
result, error = run("nexoraq.nex", script)
end_time = time.time()

if error:
    print(f"Error: {error.as_string()}")
else:
    elapsed_time = (end_time - start_time) * 1000
    print(f"\nTime elapsed: {elapsed_time:.2f} ms")

print("\n" + "=" * 50)
