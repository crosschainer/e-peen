import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import os

class CPUBenchmark():
    def __init__(self):
        self.name = "CPU Benchmark"
        self.description = "A CPU benchmark that calculates the sum of squares of numbers from 0 to 9999."

    def benchmark_task(self):
        result = sum(x * x for x in range(100000))  # Increase range to make the task more CPU intensive
        return result
    
    def run_single_thread_benchmark(self, duration=10):
        print("Running single-threaded benchmark...")
        start_time = time.time()
        iterations = 0
        
        while time.time() - start_time < duration:
            self.benchmark_task()
            iterations += 1
        
        print("Finished single-threaded benchmark")
        return iterations

    def run_multithreaded_benchmark(self, duration=10):
        print("Running multithreaded benchmark...")
        start_time = time.time()
        iterations_per_worker = 100  # Number of iterations each worker will perform before checking the time
        
        num_workers = os.cpu_count() or 1  # Use the number of CPU cores available
        
        with ThreadPoolExecutor(max_workers=num_workers) as executor:
            futures = []
            
            # Launch initial set of tasks
            for _ in range(num_workers):
                futures.append(executor.submit(self.run_benchmark_task, iterations_per_worker))
            
            total_iterations = 0
            
            while time.time() - start_time < duration:
                # Check completed tasks
                done_futures = []
                for future in as_completed(futures):
                    total_iterations += future.result()
                    done_futures.append(future)
                    # Relaunch the task if within the time limit
                    if time.time() - start_time < duration:
                        futures.append(executor.submit(self.run_benchmark_task, iterations_per_worker))
                
                # Remove completed futures
                for future in done_futures:
                    futures.remove(future)

        print("Finished multithreaded benchmark")
        return total_iterations
    
    def run_benchmark_task(self, iterations):
        count = 0
        for _ in range(iterations):
            self.benchmark_task()
            count += 1
        return count