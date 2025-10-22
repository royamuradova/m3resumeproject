# Part 3 — Runtime Measurement
import random, time
from statistics import mean
from search_algorithms import (
    recursive_binary_search,
    iterative_binary_search,
    sequential_search,
)

def time_us(fn, *args, **kwargs):
    """Return the runtime of a single call in microseconds (µs)."""
    start = time.perf_counter()
    fn(*args, **kwargs)
    end = time.perf_counter()
    return (end - start) * 1_000_000  # convert seconds to microseconds

def run_experiment(
    sizes=(5_000, 50_000, 100_000, 150_000, 1_000_000),
    trials=10
):
    print("=== PART 3: Timing Experiments (µs) ===")
    print(f"{'N':>10} | {'RBS avg':>10} | {'IBS avg':>10} | {'SEQ avg':>10}")
    print("-"*52)

    for N in sizes:
        rbs_times, ibs_times, seq_times = [], [], []

        for _ in range(trials):
            # 1) Generate data once per trial
            arr = [random.randint(1, 1_000_000) for _ in range(N)]
            arr_sorted = sorted(arr)  # needed for binary searches
            target = random.randint(1, 1_000_000)  # may hit or miss

            # 2) Measure ONLY the search calls (not the sort)
            rbs_times.append(time_us(recursive_binary_search, arr_sorted, target, 0, len(arr_sorted)-1))
            ibs_times.append(time_us(iterative_binary_search, arr_sorted, target))
            seq_times.append(time_us(sequential_search, arr_sorted, target))  # sequential on the same data

        print(f"{N:>10} | {mean(rbs_times):>10.2f} | {mean(ibs_times):>10.2f} | {mean(seq_times):>10.2f}")

if __name__ == "__main__":
    run_experiment()
