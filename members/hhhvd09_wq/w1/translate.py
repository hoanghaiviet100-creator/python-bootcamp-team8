# Sieve of Eratosthenes marks composite numbers to find primes efficiently.
def primes_up_to(n: int) -> list[int]:
    """
    Return all prime numbers from 2 to n (inclusive).

    Unlike C++ vector<bool>, Python uses a list of booleans.
    Python range(start, stop, step) replaces C++ for loops,
    with stop being exclusive.
    """
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False

    p = 2

    while p * p <= n:
        if is_prime[p]:
            for j in range(p * p, n + 1, p):
                is_prime[j] = False

        p += 1

    primes = []

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)

    return primes