"""Handles the processing of tasks in parallel."""
import multiprocessing


class TaskProcessor:
    """Class to handle Processes"""

    def __init__(self, num_tasks):
        self.num_tasks = num_tasks

    def process_task(self, task_number):
        """A sample function to perform a task."""
        print(f"Processing Task {task_number}")

    def run_parallel_tasks(self):
        """Run multiple tasks in parallel using multiprocessing."""
        processes = []

        # Create a multiprocessing pool
        with multiprocessing.Pool() as pool:
            # Distribute tasks to the pool
            for task_number in range(1, self.num_tasks + 1):
                processes.append(
                    pool.apply_async(self.process_task, args=(task_number,))
                )

            # Wait for all processes to complete
            pool.close()
            pool.join()

        # Retrieve results if needed
        results = [process.get() for process in processes]

        return results
