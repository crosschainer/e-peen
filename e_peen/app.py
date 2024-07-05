from e_peen.benchmarks.cpu import CPUBenchmark
from e_peen.benchmarks.gpu import GPUBenchmark
from e_peen.benchmarks.ram import RAMBenchmark
from e_peen.benchmarks.storage import StorageBenchmark

class App():
    def __init__(self):
        self.cpu_benchmark = CPUBenchmark()
        try:
            self.gpu_benchmark = GPUBenchmark()
        except Exception as e:
            print("GPU benchmarking is not supported on this system.")
            self.gpu_benchmark = None
        self.ram_benchmark = RAMBenchmark()
        self.storage_benchmark = StorageBenchmark()

    def run_as_cli(self):
        print("Measuring e-peen...")
        print(self.cpu_benchmark.name)
        single_thread_score = self.cpu_benchmark.run_single_thread_benchmark()
        print("CPU Single-threaded benchmark score:", single_thread_score)
        multi_thread_score = self.cpu_benchmark.run_multithreaded_benchmark()
        print("CPU Multi-threaded benchmark score:", multi_thread_score)
        gpu_score = 0
        if self.gpu_benchmark:
            print(self.gpu_benchmark.name)
            gpu_score = self.gpu_benchmark.run_benchmark()
            print("GPU benchmark score:", gpu_score)
        print(self.ram_benchmark.name)
        ram_score = self.ram_benchmark.run_benchmark()
        print("RAM benchmark score:", ram_score)
        storage_score = self.storage_benchmark.run_benchmark()
        print("Storage benchmark score:", storage_score)
        print("Total e-peen score:", single_thread_score + multi_thread_score + gpu_score + ram_score + storage_score)
        print("Finished measuring e-peen")
    
def run():
    app = App()
    app.run_as_cli()

if __name__ == "__main__":
    run()