def sieve_1(n):
    """
    Решето Эратосфена.
    :param = n:int - число до которого будет построен список простых чисел
    :return = primes:list - список простых чисел
    """
    is_prime = [True] * (n + 1)
    primes = []
    for digit in range(2, n + 1):
        if is_prime[digit]:
            primes.append(digit)
            for i in range(digit**2, n+1, digit):
                is_prime[i] = False
    return primes


print(sieve_1(1000))
