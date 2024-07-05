import time
import os
import numpy as np

class StorageBenchmark():
    def __init__(self):
        self.name = "Storage Benchmark"
        self.description = "A storage benchmark that measures the speed of reading and writing large files."

    def write_benchmark(self, file_path, size):
        data = np.random.bytes(size)
        start_time = time.time()
        with open(file_path, 'wb') as f:
            f.write(data)
        end_time = time.time()
        return end_time - start_time

    def read_benchmark(self, file_path, size):
        start_time = time.time()
        with open(file_path, 'rb') as f:
            _ = f.read(size)
        end_time = time.time()
        return end_time - start_time

    def run_benchmark(self, file_path='test_file.bin', size=1000000000):
        print("Running storage benchmark...")
        # Run write benchmark
        write_time = self.write_benchmark(file_path, size)
        # Run read benchmark
        read_time = self.read_benchmark(file_path, size)

        write_speed = size / (1024 ** 2) / write_time  # MB/s
        read_speed = size / (1024 ** 2) / read_time  # MB/s

        # Calculate the composite score: higher speeds result in higher scores
        write_score = 1 / write_time
        read_score = 1 / read_time

        composite_score = (write_score + read_score) * 1000  # Scale the score for better readability

        # Clean up the test file
        os.remove(file_path)
        
        print("Finished storage benchmark")
        return int(composite_score)