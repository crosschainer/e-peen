import time
import numpy as np

class RAMBenchmark():
    def __init__(self):
        self.name = "RAM Benchmark"
        self.description = "A RAM benchmark that measures the speed of reading, writing, and copying large arrays."

    def write_benchmark(self, size):
        a = np.zeros(size, dtype=np.float32)
        start_time = time.time()
        a[:] = 1.0  # Write operation
        end_time = time.time()
        return end_time - start_time

    def read_benchmark(self, size):
        a = np.ones(size, dtype=np.float32)
        start_time = time.time()
        _ = a.sum()  # Read operation
        end_time = time.time()
        return end_time - start_time

    def copy_benchmark(self, size):
        a = np.ones(size, dtype=np.float32)
        b = np.zeros(size, dtype=np.float32)
        start_time = time.time()
        np.copyto(b, a)  # Copy operation
        end_time = time.time()
        return end_time - start_time

    def run_benchmark(self, size=100000000):
        print("Running RAM benchmark...")
        write_time = self.write_benchmark(size)
        read_time = self.read_benchmark(size)
        copy_time = self.copy_benchmark(size)

        write_speed = size * 4 / (1024 ** 3) / write_time  # GB/s
        read_speed = size * 4 / (1024 ** 3) / read_time  # GB/s
        copy_speed = size * 4 / (1024 ** 3) / copy_time  # GB/s

        # Calculate the composite score: higher speeds result in higher scores
        write_score = 1 / write_time
        read_score = 1 / read_time
        copy_score = 1 / copy_time

        composite_score = (write_score + read_score + copy_score) * 1000  # Scale the score for better readability

        print("Finished RAM benchmark")
        return int(composite_score)