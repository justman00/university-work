def first_primes(n):
    i = 1
    res = []
    while len(res) != n:
        if is_prime(i):
            res.append(i)
        i = i + 1

    return res


def is_prime(num):
    if num < 3:
        return True

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


print(first_primes(1024))
