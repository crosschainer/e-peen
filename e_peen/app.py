from e_peen.benchmarks.cpu import CPUBenchmark
from e_peen.benchmarks.gpu import GPUBenchmark
from e_peen.benchmarks.ram import RAMBenchmark
from e_peen.benchmarks.storage import StorageBenchmark

from rich.console import Console
from rich.table import Table

class App():
    def __init__(self):
        try:
            self.cpu_benchmark = CPUBenchmark()
        except Exception as e:
            self.cpu_benchmark = None
        try:
            self.gpu_benchmark = GPUBenchmark()
        except Exception as e:
            self.gpu_benchmark = None
        try:
            self.ram_benchmark = RAMBenchmark()
        except Exception as e:
            self.ram_benchmark = None
        try:
            self.storage_benchmark = StorageBenchmark()
        except Exception as e:
            self.storage_benchmark = None

        self.console = Console()

    def run_as_cli(self):
        self.console.print("[bold magenta]Measuring e-peen...[/bold magenta]\n")

        # Create a table to display benchmark results
        table = Table(title="Benchmark Results")

        table.add_column("Benchmark", justify="left", style="cyan", no_wrap=True)
        table.add_column("Result", justify="right", style="yellow")

        total_score = 0

        if self.cpu_benchmark:
            try:
                self.console.print(f"[bold cyan]{self.cpu_benchmark.name}[/bold cyan]\nRunning...")
                single_thread_score = self.cpu_benchmark.run_single_thread_benchmark()
                multi_thread_score = self.cpu_benchmark.run_multithreaded_benchmark()
                table.add_row("CPU Single-threaded", f"{single_thread_score:.2f}")
                table.add_row("CPU Multi-threaded", f"{multi_thread_score:.2f}")
                total_score += single_thread_score + multi_thread_score
            except Exception as e:
                self.console.print(f"[bold red]CPU Benchmark failed: {e}[/bold red]\n")
        else:
            self.console.print("[bold red]CPU Benchmark not supported[/bold red]\n")

        if self.gpu_benchmark:
            try:
                self.console.print(f"[bold cyan]{self.gpu_benchmark.name}[/bold cyan]\nRunning...")
                gpu_score = self.gpu_benchmark.run_benchmark()
                table.add_row("GPU", f"{gpu_score:.2f}")
                total_score += gpu_score
            except Exception as e:
                self.console.print(f"[bold red]GPU Benchmark failed: {e}[/bold red]\n")
        else:
            self.console.print("[bold red]GPU Benchmark not supported[/bold red]\n")

        if self.ram_benchmark:
            try:
                self.console.print(f"[bold cyan]{self.ram_benchmark.name}[/bold cyan]\nRunning...")
                ram_results = self.ram_benchmark.run_benchmark()
                table.add_row("RAM Write Speed", f"{ram_results['write_speed']:.2f} GB/s")
                table.add_row("RAM Read Speed", f"{ram_results['read_speed']:.2f} GB/s")
                table.add_row("RAM Copy Speed", f"{ram_results['copy_speed']:.2f} GB/s")
                table.add_row("RAM Composite Score", f"{ram_results['composite_score']:.2f}")
                total_score += ram_results['composite_score']
            except Exception as e:
                self.console.print(f"[bold red]RAM Benchmark failed: {e}[/bold red]\n")
        else:
            self.console.print("[bold red]RAM Benchmark not supported[/bold red]\n")

        if self.storage_benchmark:
            try:
                self.console.print(f"[bold cyan]{self.storage_benchmark.name}[/bold cyan]\nRunning...")
                storage_results = self.storage_benchmark.run_benchmark()
                table.add_row("Storage Write Speed", f"{storage_results['write_speed']:.2f} MB/s")
                table.add_row("Storage Read Speed", f"{storage_results['read_speed']:.2f} MB/s")
                table.add_row("Storage Composite Score", f"{storage_results['composite_score']:.2f}")
                total_score += storage_results['composite_score']
            except Exception as e:
                self.console.print(f"[bold red]Storage Benchmark failed: {e}[/bold red]\n")
        else:
            self.console.print("[bold red]Storage Benchmark not supported[/bold red]\n")

        # Total composite score
        table.add_row("Total Composite Score", f"{total_score}")

        # Display the results table
        self.console.print(table)

def run():
    app = App()
    app.run_as_cli()

if __name__ == "__main__":
    run()
