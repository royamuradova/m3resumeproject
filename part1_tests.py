from search_algorithms import recursive_binary_search, iterative_binary_search, sequential_search

def run_small_tests():
    print("=== PART 1: Small tests ===")
    arr_sorted = [3, 5, 8, 12, 14, 18, 21]
    target_hit = 12
    target_miss = 9

    print("\n-- Existing target (12) --")
    print("recursive_binary_search ->", recursive_binary_search(arr_sorted, target_hit, 0, len(arr_sorted)-1))
    print("iterative_binary_search ->", iterative_binary_search(arr_sorted, target_hit))
    print("sequential_search      ->", sequential_search(arr_sorted, target_hit))

    print("\n-- Target does not exist (9) --")
    print("recursive_binary_search ->", recursive_binary_search(arr_sorted, target_miss, 0, len(arr_sorted)-1))
    print("iterative_binary_search ->", iterative_binary_search(arr_sorted, target_miss))
    print("sequential_search      ->", sequential_search(arr_sorted, target_miss))
    # This line makes sure that when we run the file directly,
    # the run_small_tests() function will execute automatically.

if __name__ == "__main__":
    run_small_tests()
