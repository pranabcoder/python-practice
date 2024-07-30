# When to Use Multithreading

# Multithreading is great for I/O-bound tasks(e.g. file operation, networking), but it's not good for CPU-bound tasks.
# I/O-bound tasks are those that spend most of their time waiting for input/output operations to complete.
# Concurrent I/O-bound tasks can be executed in parallel using multithreading.

import threading
import time


def print_numbers():
    for i in range(1, 6):
        time.sleep(2)
        print(f"Numbers : {i}")


def print_letters():
    for letter in 'abcde':
        time.sleep(2)
        print(f"Letters : {letter}")


# Create two threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)
t = time.time()
# Start the threads
t1.start()
t2.start()
# Wait for the threads to finish
t1.join()
t2.join()
finished_time = time.time() - t
print(f'Finished in {finished_time} seconds')
