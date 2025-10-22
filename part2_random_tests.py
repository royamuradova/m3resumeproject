# Import Python's built-in 'random' module for generating random numbers
import random

# Import all three search algorithms from your previous file
from search_algorithms import (
    recursive_binary_search,
    iterative_binary_search,
    sequential_search,
)

# Define one test function that performs a single randomized trial
def one_trial(n=30):
    # 1️⃣ Create a random list with n elements
    # Each element is a random integer between 1 and 1000
    arr = [random.randint(1, 1000) for _ in range(n)]

    # 2️⃣ Choose a target number
    # 50% of the time, the target will exist in the list (HIT)
    # The other 50% of the time, the target will not exist (MISS)
    if random.random() < 0.5:
        target = random.choice(arr)   # pick a random element from the list
        label = "HIT"
    else:
        target = 10_000_000           # very large number, definitely not in list
        label = "MISS"

    # 3️⃣ Sort the list for binary search (binary requires a sorted array)
    arr_sorted = sorted(arr)

    # 4️⃣ Run all three search algorithms
    # Sequential search can work on unsorted lists
    seq_res = sequential_search(arr, target)

    # Binary searches require the sorted version of the list
    rbs_res = recursive_binary_search(arr_sorted, target, 0, len(arr_sorted)-1)
    ibs_res = iterative_binary_search(arr_sorted, target)

    # 5️⃣ Print the results in one formatted line
    print(f"[{label}] target={target:>7} | Seq={seq_res}  RBS={rbs_res}  IBS={ibs_res}")

    # 6️⃣ Verify that all three algorithms agree
    # If any result is different, an AssertionError will stop the program
    assert bool(seq_res) == bool(rbs_res) == bool(ibs_res), "Results do not match!"

# Define a main function that runs multiple trials
def main():
    print("=== PART 2: Randomized Testing ===")
    # Repeat the random test 12 times
    for _ in range(12):
        one_trial(n=40)   # each trial uses a list of 40 random numbers

# Run the main function automatically when this file is executed
if __name__ == "__main__":
    main()
