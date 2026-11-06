import time

naive_calls = 0


def ways_naive(n):
    global naive_calls
    naive_calls += 1

    if n <= 1:
        return 1

    return ways_naive(n - 1) + ways_naive(n - 2)


def ways_iterative(n):
    if n <= 1:
        return 1, 0

    previous = 1
    current = 1
    iterations = 0

    for step in range(2, n + 1):
        next_value = previous + current
        previous = current
        current = next_value
        iterations += 1

    return current, iterations


def measure_naive(n):
    global naive_calls
    naive_calls = 0

    start = time.perf_counter()
    result = ways_naive(n)
    elapsed = time.perf_counter() - start

    return result, naive_calls, elapsed


def measure_iterative(n):
    start = time.perf_counter()
    result, iterations = ways_iterative(n)
    elapsed = time.perf_counter() - start

    return result, iterations, elapsed


def main():
    print("CO2 - Q7: DIAGNOSE, REDESIGN AND VALIDATE")
    print("Selected program: Q6 - Counting ways to climb temple steps")
    print()

    print("A. DIAGNOSE THE BOTTLENECK")
    print("The original recursive function calls itself twice for most values of n.")
    print("It recalculates the same smaller stair counts many times.")
    print("The number of function calls grows exponentially as n increases.")
    print()

    print("B. DESIGN OBJECTIVE")
    print("Calculate the same answer in O(n) time and O(1) extra space.")
    print()

    print("C. REVISED DESIGN")
    print("Keep only the previous two answers and calculate the next answer in a loop.")
    print("This avoids repeated recursive calls and does not need a cache.")
    print("Trade-off: the iterative version is less direct than the recursive definition.")
    print()
    print("Pseudocode:")
    print("1. Set previous = 1 and current = 1.")
    print("2. Repeat from step 2 to n.")
    print("3. Calculate next = previous + current.")
    print("4. Move current into previous and next into current.")
    print("5. Return current.")
    print()

    print("D. PREDICTION")
    print("The iterative version should use n-1 loop iterations and O(1) extra space.")
    print("It should be much faster than plain recursion for larger n.")
    print()

    print("E. IMPLEMENTATION AND VALIDATION")
    print("Both versions are tested with the same inputs.")
    print("Times are measured on the computer running this program.")
    print()
    print(f"{'n':>5} {'Answer':>15} {'Naive calls':>15} {'Naive time (s)':>16} "
          f"{'Loop iterations':>17} {'Loop time (s)':>15}")

    for n in (10, 20, 25, 30):
        naive_result, calls, naive_time = measure_naive(n)
        loop_result, iterations, loop_time = measure_iterative(n)

        if naive_result != loop_result:
            print("Validation failed: answers do not match.")
            return

        print(f"{n:5d} {naive_result:15d} {calls:15d} {naive_time:16.8f} "
              f"{iterations:17d} {loop_time:15.8f}")

    print()
    print("Validation: Both methods produced identical answers for every test input.")
    print()

    print("Large input test:")
    large_result, large_iterations = ways_iterative(1000)
    print("n = 1000")
    print("Answer calculated successfully.")
    print("Number of loop iterations:", large_iterations)
    print("Number of digits in answer:", len(str(large_result)))
    print()

    print("F. FINAL EVALUATION")
    print("The redesign meets the objective: it calculates the same result using O(n) time")
    print("and O(1) extra space, without recursive calls or a cache.")
    print("Plain recursion is useful for demonstrating the mathematical definition and")
    print("small inputs, but the iterative version is more suitable for large staircases.")
    print()
    print("Complexity comparison:")
    print("Plain recursion: O(2^n) time and O(n) call-stack space.")
    print("Iterative redesign: O(n) time and O(1) extra space.")


if __name__ == "__main__":
    main()
