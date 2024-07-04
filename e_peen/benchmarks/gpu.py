import time
import numpy as np
import pyopencl as cl

class GPUBenchmark():
    def __init__(self):
        self.name = "GPU Benchmark"
        self.description = "A GPU benchmark that calculates the sum of squares of numbers using PyOpenCL."

        # Set up OpenCL context and queue
        platforms = cl.get_platforms()
        self.device = platforms[0].get_devices()[0]
        self.context = cl.Context([self.device])
        self.queue = cl.CommandQueue(self.context)

        # Kernel code
        self.kernel_code = """
        __kernel void sum_squares(__global const float *a, __global float *result) {
            int gid = get_global_id(0);
            result[gid] = a[gid] * a[gid];
        }
        """
        self.program = cl.Program(self.context, self.kernel_code).build()

    def benchmark_task(self):
        # Example task: calculating sum of squares on the GPU
        n = 1000000
        a_np = np.arange(n, dtype=np.float32)
        result_np = np.zeros_like(a_np)

        mf = cl.mem_flags
        a_g = cl.Buffer(self.context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a_np)
        result_g = cl.Buffer(self.context, mf.WRITE_ONLY, result_np.nbytes)

        kernel = self.program.sum_squares
        kernel.set_arg(0, a_g)
        kernel.set_arg(1, result_g)

        cl.enqueue_nd_range_kernel(self.queue, kernel, (n,), None)
        cl.enqueue_copy(self.queue, result_np, result_g)
        self.queue.finish()

        return np.sum(result_np)
    
    def run_benchmark(self, duration=10):
        print("Running GPU benchmark...")
        start_time = time.time()
        iterations = 0
        
        while time.time() - start_time < duration:
            self.benchmark_task()
            iterations += 1

        print("Finished GPU benchmark")
        return iterations