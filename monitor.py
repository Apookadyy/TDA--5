import time
import psutil


def log_execution_time(start_time):
    """
    Log execution time of a process
    """
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution Time: {execution_time:.4f} seconds")


def system_usage():
    """
    Display CPU and memory usage
    """
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")

    return {
        "cpu": cpu,
        "memory": memory
    }