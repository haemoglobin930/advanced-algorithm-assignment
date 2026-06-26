from dataclasses import dataclass
from threading import Thread
from time import perf_counter_ns


@dataclass
class FactorialResult:
    number: int
    value: int
    start_ns: int
    end_ns: int

    @property
    def duration_ns(self) -> int:
        return self.end_ns - self.start_ns


def factorial_number(number: int) -> int:
    result = 1
    for multiplier in range(2, number + 1):
        result *= multiplier
    return result


def factorial_worker(number: int, results: dict[int, FactorialResult]) -> None:
    start_ns = perf_counter_ns()
    value = factorial_number(number)
    end_ns = perf_counter_ns()
    results[number] = FactorialResult(number, value, start_ns, end_ns)


def run_threaded_round(numbers: list[int]) -> tuple[int, dict[int, FactorialResult]]:
    results: dict[int, FactorialResult] = {}
    threads: list[Thread] = []

    for number in numbers:
        thread = Thread(target=factorial_worker, args=(number, results))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    first_start = min(result.start_ns for result in results.values())
    last_end = max(result.end_ns for result in results.values())
    return last_end - first_start, results


def run_sequential_round(numbers: list[int]) -> tuple[int, dict[int, FactorialResult]]:
    results: dict[int, FactorialResult] = {}
    first_start = perf_counter_ns()

    for number in numbers:
        start_ns = perf_counter_ns()
        value = factorial_number(number)
        end_ns = perf_counter_ns()
        results[number] = FactorialResult(number, value, start_ns, end_ns)

    last_end = perf_counter_ns()
    return last_end - first_start, results


def run_experiment(rounds: int = 10) -> tuple[list[int], list[int]]:
    numbers = [50, 100, 200]
    threaded_times: list[int] = []
    sequential_times: list[int] = []

    print("\nMULTITHREADING FACTORIAL EXPERIMENT")
    print("-" * 64)
    for round_number in range(1, rounds + 1):
        total_ns, results = run_threaded_round(numbers)
        threaded_times.append(total_ns)
        print(f"Round {round_number:02d} threaded total time (ns): {total_ns}")

    threaded_average = sum(threaded_times) / len(threaded_times)
    print(f"Threaded average time (ns): {threaded_average:.2f}")
    print_result_summary(results)

    print("\nSEQUENTIAL FACTORIAL EXPERIMENT")
    print("-" * 64)
    for round_number in range(1, rounds + 1):
        total_ns, results = run_sequential_round(numbers)
        sequential_times.append(total_ns)
        print(f"Round {round_number:02d} sequential total time (ns): {total_ns}")

    sequential_average = sum(sequential_times) / len(sequential_times)
    print(f"Sequential average time (ns): {sequential_average:.2f}")
    print_result_summary(results)

    print("\nCOMPARISON")
    print("-" * 64)
    print(f"Threaded average (ns)  : {threaded_average:.2f}")
    print(f"Sequential average (ns): {sequential_average:.2f}")
    if threaded_average < sequential_average:
        print("Result: multithreading was faster in this run.")
    else:
        print("Result: sequential execution was faster in this run.")

    return threaded_times, sequential_times


def print_result_summary(results: dict[int, FactorialResult]) -> None:
    print("Factorial result summary:")
    for number in sorted(results):
        value = results[number].value
        print(f"{number}! has {len(str(value))} digits")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Factorial threading experiment")
    parser.add_argument("--demo", action="store_true", help="Run 10-round timing experiment")
    args = parser.parse_args()

    if args.demo:
        run_experiment(rounds=10)
    else:
        run_experiment(rounds=10)
