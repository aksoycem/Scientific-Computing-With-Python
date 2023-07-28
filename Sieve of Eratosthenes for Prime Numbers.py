def find_prime_numbers(n):
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    prime_numbers = [i for i in range(2, n + 1) if primes[i]]
    return prime_numbers

if __name__ == "__main__":
    upper_limit = int(input("Enter the upper limit to find prime numbers: "))
    prime_numbers = find_prime_numbers(upper_limit)
    print("Prime Numbers:", prime_numbers)
