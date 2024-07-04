from e_peen.benchmarks.cpu import CPUBenchmark
from e_peen.benchmarks.gpu import GPUBenchmark

class App():
    def __init__(self):
        self.cpu_benchmark = CPUBenchmark()
        self.gpu_benchmark = GPUBenchmark()

    def run_as_cli(self):
        print("Measuring e-peen...")
        print(self.cpu_benchmark.name)
        print("CPU Single-threaded benchmark score:", self.cpu_benchmark.run_single_thread_benchmark())
        print("CPU Multi-threaded benchmark score:", self.cpu_benchmark.run_multithreaded_benchmark())
        print(self.gpu_benchmark.name)
        print("GPU benchmark score:", self.gpu_benchmark.run_benchmark())

    
def run():
    app = App()
    app.run_as_cli()

if __name__ == "__main__":
    run()