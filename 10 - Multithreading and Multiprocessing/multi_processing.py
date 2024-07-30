"""Multiprocessing - a Process that runs in parallel,
CPU - Bound tasks - that are heavy on CPU usage (e.g.,
video processing, image processing, mathematical calculations, data processing)
Parallel execution - multiple cores of the CPU are used to execute the tasks"""
import multiprocessing
import time


def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i * i}")


def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i * i * i}")


if __name__ == "__main__":
    # create 2 processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)
    t = time.time()

    # start the process
    p1.start()
    p2.start()

    # Wait for the process to complete
    p1.join()
    p2.join()

    finished_time = time.time() - t
    print(finished_time)
