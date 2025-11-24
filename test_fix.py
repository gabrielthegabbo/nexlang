import run
import os

# Ensure we are in the right directory for relative paths
if os.path.exists("nexoraq.myopl"):
    print("Found nexoraq.myopl")
else:
    print("Warning: nexoraq.myopl not found")

# This simulates typing RUN("nexoraq.myopl") in the shell
print("Executing RUN('nexoraq.myopl')...")
result, error = run.run('<stdin>', 'RUN("nexoraq.myopl")')

if error:
    print("Error occurred:")
    print(error.as_string())
else:
    print("Execution successful!")
